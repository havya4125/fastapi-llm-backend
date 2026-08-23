import os

from anthropic import Anthropic
from dotenv import load_dotenv

from ..schemas.task import TaskSuggestion
from ..tools.tasks_tools import create_task_tool

load_dotenv()
client = Anthropic(
    api_key= os.environ.get("ANTHROPIC_API_KEY")
)

tools = [
    {
        "name": "create_task",
        "description": "Create a new task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title of the task."
                },
                "priority": {
                    "type": "string",
                    "description": "The priority of the task."
                },
                "description": {
                    "type": "string",
                    "description": "The description of the task."
                }
            },
            "required": ["title", "priority"]
        }
    }
]

def ask_claude(messages, system_prompt: str | None = None):
    params = {
        "model" : 'claude-sonnet-4-5',
        "max_tokens" : 1024,
        "messages" : messages,
    }
    if(system_prompt):
        params["system"] = system_prompt

    response = client.messages.create(**params)
    return response.content[0].text

def stream_claude(messages, system_prompt: str | None = None):
    params = {
        "model" : "claude-sonnet-4-5",
        "max_tokens" : 1024,
        "messages" : messages
    }
    if(system_prompt):
        params["system"] = system_prompt
    
    with client.messages.stream(**params) as stream:
        yield from stream.text_stream

def generate_task_suggestion(messages):
    response = client.messages.parse(
        model='claude-haiku-4-5',
        max_tokens=1024,
        messages= messages,
        output_format=TaskSuggestion
    )
    return response.parsed_output

def claude():
    response = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=1024,
        messages= [{
            "role" : "user",
            "content" : "Create me a task to learn fast api"
        }],
        tools=tools
    )
    tool_call = response.content[0]
    print(tool_call.name)
    print(tool_call.input)
    result = create_task_tool(** tool_call.input)
    print(result)

if __name__ == "__main__":
    claude()