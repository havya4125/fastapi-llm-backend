import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(
    api_key= os.environ.get("ANTHROPIC_API_KEY")
)

def ask_claude(message: str):
    response = client.messages.create(
        model = 'claude-sonnet-4-5',
        max_tokens= 1024,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.content[0].text