from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    title: str
    description: str | None = None
    priority: str


class UpdateTaskRequest(BaseModel):
    title: str
    description: str
    priority: str
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: str
    completed: bool

class TaskSuggestion(BaseModel):
    title: str
    priority: str
    estimated_hours: int

class TaskSuggestionRequest(BaseModel):
    message: str