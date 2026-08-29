from pydantic import BaseModel

from .task import TaskResponse


class AgentRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class AgentData(BaseModel):
    task: TaskResponse | None = None
    tasks: list[TaskResponse] | None = None


class AgentResult(BaseModel):
    message: str
    action: str
    data: AgentData | None = None


class AgentResponse(BaseModel):
    conversation_id: str
    message: str
    action: str
    data: AgentData | None = None
