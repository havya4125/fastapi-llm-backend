from ..schemas.chat import ChatRequest
from ..services.claude_service import ask_claude


#Handler for POST chat
def chat(request : ChatRequest):
    response = ask_claude(request.message)

    return {
        "response" : response
    } 