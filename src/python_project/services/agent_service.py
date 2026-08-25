
from ..schemas.agent import AgentResponse, AgentResult
from ..store.conversation_store import (
    create_conversation,
    get_conversation,
    save_conversation,
)
from ..tools.registry import tool_registry
from ..tools.tool_definitions import task_tools
from ..utils import append_assistant_message, append_user_message
from .claude_service import ask_claude, generate_structured_response

system_prompt = """
You are an instructor who helps the user plan, create, and manage their tasks and assignments.
Guide the user with practical suggestions, help them break down larger tasks into smaller steps,
and assist them in organizing their work effectively.
"""
MAX_TOOL_ITERATIONS = 5
#Handler for agent Orchestration
def run_agent(message: str, conversation_id: str | None = None):
    if conversation_id :
        messages = get_conversation(conversation_id)
    else:
        conversation_id = create_conversation()
        messages = []

    append_user_message(messages, message)
    for _ in range(MAX_TOOL_ITERATIONS):
        response = ask_claude(messages, system_prompt, task_tools)

        if response.stop_reason != "tool_use":
            final_structured_response = generate_structured_response(messages, AgentResult)
            append_assistant_message(messages, final_structured_response.model_dump_json())
            save_conversation(conversation_id, messages)
            return AgentResponse(
                conversation_id=conversation_id,
                message=final_structured_response.message,
                action=final_structured_response.action,
                data=final_structured_response.data
            )
    
        tool_results = []

        for block in response.content:
        
            if block.type != 'tool_use':
                continue
            tool_function = tool_registry.get(block.name)
            result = tool_function(**block.input)
            tool_results.append({
                "type":"tool_result",
                "tool_use_id" : block.id,
                "content" : str(result)
                })
        append_assistant_message(messages, response.content)
        append_user_message(messages, tool_results)
    return "I couldn't complete the request within the allowed number of tool calls."
