from fastapi import APIRouter

from ..handlers.agent_handlers import agent_handler
from ..schemas.agent import AgentRequest, AgentResponse

router = APIRouter()

@router.post('/agent', response_model= AgentResponse, status_code=201)
def agent_route(request: AgentRequest):
    return agent_handler(request)