from fastapi import APIRouter

from ..handlers.chat_handlers import chat, chat_stream
from ..schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post('/chat', response_model=ChatResponse)
def chat_route(request: ChatRequest):
    return chat(request)

@router.post('/chat/stream')
def chat_stream_route(request: ChatRequest):
    return chat_stream(request)