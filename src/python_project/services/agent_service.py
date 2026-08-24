from ..tools.registry import tool_registry
from ..tools.tool_definitions import task_tools
from ..utils import append_assistant_message, append_user_message
from .claude_service import ask_claude

system_prompt = """
You are an instructor who helps the user plan, create, and manage their tasks and assignments.
Guide the user with practical suggestions, help them break down larger tasks into smaller steps,
and assist them in organizing their work effectively.
"""
#Handler for agent Orchestration
def run_agent(message: str):
    messages = []
    append_user_message(messages, message)
    response = ask_claude(messages, system_prompt, task_tools)
    print(response)
    tool_call = response.content[0]
    tool_function = tool_registry[tool_call.name]
    result = tool_function(**tool_call.input)
    append_assistant_message(messages, response.content)
    messages.append({
        "role": "user",
        "content": [
            {
                "type": "tool_result",
                "tool_use_id": tool_call.id,
                "content" : str(result)
            }
        ]
    })
    final_response = ask_claude(messages, system_prompt, task_tools)
    return final_response.content[0].text