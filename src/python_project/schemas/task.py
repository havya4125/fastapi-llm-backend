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