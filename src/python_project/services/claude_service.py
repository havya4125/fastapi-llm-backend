import os

from anthropic import Anthropic
from dotenv import load_dotenv

from ..schemas.task import TaskSuggestion

load_dotenv()
client = Anthropic(
    api_key= os.environ.get("ANTHROPIC_API_KEY")
)

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