from pydantic import BaseModel

from .task import TaskResponse


class AgentRequest(BaseModel):
    message: str

class AgentData(BaseModel):
    task: TaskResponse | None = None
    tasks: list[TaskResponse] | None = None

class AgentResponse(BaseModel):
    message: str
    action: str
    data: AgentData | None = None