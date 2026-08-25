from ..schemas.agent import AgentRequest
from ..services.agent_service import run_agent


#Handler for agent route
def agent_handler(request: AgentRequest):
    return run_agent(request.message, request.conversation_id)