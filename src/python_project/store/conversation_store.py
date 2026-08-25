from uuid import uuid4

from .exception import ConversationNotFoundEror

conversations: dict[str, list] = {}

def create_conversation() -> str:
    conversation_id = str(uuid4())
    conversations[conversation_id] = []

    return conversation_id

def get_conversation(conversation_id : str) -> list:
    if conversation_id not in conversations:
        raise ConversationNotFoundEror(
            f"Conversation {conversation_id} not found"
        )
    return conversations[conversation_id]

def save_conversation(conversation_id : str, messages: list) -> None:
    conversations[conversation_id] = messages