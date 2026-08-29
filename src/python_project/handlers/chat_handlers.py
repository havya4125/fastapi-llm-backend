import uuid

from fastapi import HTTPException
from fastapi.sse import ServerSentEvent

from ..schemas.chat import ChatRequest
from ..services.claude_service import ask_claude, stream_claude
from ..utils import append_assistant_message, append_user_message

conversations = {}


# Handler for POST chat
def chat(request: ChatRequest):
    conversation_id = request.conversation_id

    if conversation_id:
        if conversation_id not in conversations:
            raise HTTPException(
                status_code=404,
                detail=f"No conversation found with conversationID {conversation_id}",
            )
        messages = conversations[conversation_id]
    else:
        conversation_id = str(uuid.uuid4())
        messages = []

    append_user_message(messages, request.message)
    system_prompt = "You are a helpful assistant. Keep your answers concise"
    response = ask_claude(messages, system_prompt)
    append_assistant_message(messages, response)
    conversations[conversation_id] = messages
    return {"conversation_id": conversation_id, "response": response}


# handler for Chat stream
def chat_stream(request: ChatRequest):
    conversation_id = request.conversation_id

    if conversation_id:
        if conversation_id not in conversations:
            raise HTTPException(
                status_code=404,
                detail=f"No conversation found with conversationID {conversation_id}",
            )
        messages = conversations[conversation_id]
    else:
        conversation_id = str(uuid.uuid4())
        messages = []
    messages = []
    append_user_message(messages, request.message)
    system_prompt = "You are a helpful assistant. Keep your answers concise"
    stream_response = stream_claude(messages, system_prompt)

    def generate():
        full_response = ""

        yield ServerSentEvent(
            event="conversation", data={"conversation_id": conversation_id}
        )
        for chunk in stream_response:
            full_response += chunk
            yield ServerSentEvent(event="message", data={"content": chunk})
        append_assistant_message(messages, full_response)
        conversations[conversation_id] = messages

        yield ServerSentEvent(event="done", data={"conversation_id": conversation_id})

    return generate()
