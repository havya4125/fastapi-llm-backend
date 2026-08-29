from fastapi import APIRouter
from fastapi.sse import EventSourceResponse

from ..handlers.chat_handlers import chat, chat_stream
from ..schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_route(request: ChatRequest):
    return chat(request)


@router.post("/chat/stream", response_class=EventSourceResponse)
def chat_stream_route(request: ChatRequest):
    return chat_stream(request)
