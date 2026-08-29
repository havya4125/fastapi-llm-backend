from ..schemas.agent import AgentRequest
from ..services.agent_service import run_agent, run_agent_stream


# Handler for agent route
def agent_handler(request: AgentRequest):
    return run_agent(request.message, request.conversation_id)


def agent_stream_handler(request: AgentRequest):
    return run_agent_stream(request.message, request.conversation_id)
