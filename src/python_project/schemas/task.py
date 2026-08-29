from typing import Literal

from pydantic import BaseModel, Field


class CreateTaskRequest(BaseModel):
    title: str = Field(min_length=1)
    description: str | None = None
    priority: Literal["low", "medium", "high"]


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


class UpdateToolTaskRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: Literal["low", "medium", "high"] | None = None
    completed: bool | None = None
