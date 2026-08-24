from ..schemas.agent import AgentRequest, AgentResponse
from ..services.agent_service import run_agent


#Handler for agent route
def agent_handler(request: AgentRequest):
    response = run_agent(request.message)
    return AgentResponse(
        response= response
    )