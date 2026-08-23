from fastapi import APIRouter

from ..handlers.agent_handlers import agent_handler
from ..schemas.agent import AgentRequest

router = APIRouter()

@router.post('/agent')
def agent_route(request: AgentRequest):
    return agent_handler(request)