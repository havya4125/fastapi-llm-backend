import os

from anthropic import Anthropic
from dotenv import load_dotenv
from pydantic import BaseModel

from ..schemas.task import TaskSuggestion

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

tools = [
    {
        "name": "create_task",
        "description": "Create a new task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The title of the task."},
                "priority": {
                    "type": "string",
                    "description": "The priority of the task.",
                },
                "description": {
                    "type": "string",
                    "description": "The description of the task.",
                },
            },
            "required": ["title", "priority"],
        },
    }
]


def ask_claude(messages, system_prompt: str | None = None, tools: list | None = None):
    params = {
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": messages,
    }
    if system_prompt:
        params["system"] = system_prompt
    if tools:
        params["tools"] = tools
    response = client.messages.create(**params)
    return response


def stream_claude(
    messages, system_prompt: str | None = None, tools: list | None = None
):
    params = {"model": "claude-sonnet-4-5", "max_tokens": 1024, "messages": messages}
    if system_prompt:
        params["system"] = system_prompt

    if tools:
        params["tools"] = tools

    with client.messages.stream(**params) as stream:
        yield from stream


def generate_task_suggestion(messages):
    response = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=messages,
        output_format=TaskSuggestion,
    )
    return response.parsed_output


def generate_structured_response(
    messages: list, output_format: type[BaseModel] | None = None
):
    params = {"model": "claude-haiku-4-5", "max_tokens": 1024, "messages": messages}
    if output_format:
        params["output_format"] = output_format
    response = client.messages.parse(**params)
    return response.parsed_output
