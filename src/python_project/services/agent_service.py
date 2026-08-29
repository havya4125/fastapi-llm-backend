import json

from fastapi.sse import ServerSentEvent

from ..exceptions.task_exceptions import TaskNotFoundError
from ..exceptions.tool_exceptions import ToolNotfoundError
from ..schemas.agent import AgentResponse, AgentResult
from ..store.conversation_store import (
    create_conversation,
    get_conversation,
    save_conversation,
)
from ..tools.registry import tool_registry
from ..tools.tool_definitions import task_tools
from ..utils import append_assistant_message, append_user_message
from .claude_service import ask_claude, generate_structured_response, stream_claude

system_prompt = """
You are an instructor who helps the user plan, create, and manage their tasks and assignments.
Guide the user with practical suggestions, help them break down larger tasks into smaller steps,
and assist them in organizing their work effectively.
"""
MAX_TOOL_ITERATIONS = 5


# Handler for agent Orchestration
def run_agent(message: str, conversation_id: str | None = None):
    if conversation_id:
        messages = get_conversation(conversation_id)
    else:
        conversation_id = create_conversation()
        messages = []

    append_user_message(messages, message)
    for _ in range(MAX_TOOL_ITERATIONS):
        response = ask_claude(messages, system_prompt, task_tools)

        if response.stop_reason != "tool_use":
            final_structured_response = generate_structured_response(
                messages, AgentResult
            )
            append_assistant_message(
                messages, final_structured_response.model_dump_json()
            )
            save_conversation(conversation_id, messages)
            return AgentResponse(
                conversation_id=conversation_id,
                message=final_structured_response.message,
                action=final_structured_response.action,
                data=final_structured_response.data,
            )

        tool_results = []

        for block in response.content:
            if block.type != "tool_use":
                continue
            tool_function = tool_registry.get(block.name)
            if tool_function is None:
                raise ToolNotfoundError(f"Tool '{block.name}' is not registered")
            try:
                result = tool_function(**block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    }
                )
            except TaskNotFoundError as err:
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(err),
                        "is_error": True,
                    }
                )
        append_assistant_message(messages, response.content)
        append_user_message(messages, tool_results)
    return "I couldn't complete the request within the allowed number of tool calls."


def run_agent_stream(message: str, conversation_id: str | None = None):
    if conversation_id:
        messages = get_conversation(conversation_id)
    else:
        conversation_id = create_conversation()
        messages = []

    append_user_message(messages, message)

    yield ServerSentEvent(
        event="conversation", data={"conversation_id": conversation_id}
    )
    for _ in range(MAX_TOOL_ITERATIONS):
        stream_response = stream_claude(messages, system_prompt, task_tools)

        assistant_content = []
        tool_calls = []
        tool_results = []

        current_tool = None

        for event in stream_response:
            if event.type == "content_block_start":
                block = event.content_block

                if block.type == "text":
                    assistant_content.append(
                        {
                            "type": "text",
                            "text": "",
                        }
                    )
                elif block.type == "tool_use":
                    current_tool = {
                        "id": block.id,
                        "name": block.name,
                        "input": "",
                    }

                    assistant_content.append(
                        {
                            "type": "tool_use",
                            "id": block.id,
                            "name": block.name,
                            "input": {},
                        }
                    )

            elif event.type == "content_block_delta":
                if event.delta.type == "text_delta":
                    assistant_content[-1]["text"] += event.delta.text

                    yield ServerSentEvent(
                        event="message", data={"content": event.delta.text}
                    )

                elif event.delta.type == "input_json_delta":
                    current_tool["input"] += event.delta.partial_json

            elif event.type == "content_block_stop":
                if current_tool:
                    if current_tool["input"]:
                        tool_input_data = json.loads(current_tool["input"])
                    else:
                        tool_input_data = {}

                    tool_calls.append(current_tool)
                    tool_function = tool_registry.get(current_tool["name"])

                    if tool_function is None:
                        raise ToolNotfoundError(
                            f"Tool '{current_tool['name']}' is not registered"
                        )

                    try:
                        result = tool_function(**tool_input_data)
                    except TaskNotFoundError as err:
                        result = str(err)

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": current_tool["id"],
                            "content": str(result),
                        }
                    )

                    assistant_content[-1]["input"] = tool_input_data

                    current_tool = None

        # After the entire claude response is processed
        append_assistant_message(messages, assistant_content)

        if not tool_results:
            break
        append_user_message(messages, tool_results)

    save_conversation(conversation_id, messages)

    yield ServerSentEvent(event="done", data={"comversation_id", conversation_id})
