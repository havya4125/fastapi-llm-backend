from fastapi import APIRouter

from ..handlers.suggestion_handlers import task_suggestion
from ..handlers.tasks_handlers import (
    create_task,
    delete_single_task,
    get_all_tasks,
    get_single_task,
    update_single_task,
)
from ..schemas.task import (
    CreateTaskRequest,
    TaskResponse,
    TaskSuggestion,
    TaskSuggestionRequest,
    UpdateTaskRequest,
)

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task_route(task: CreateTaskRequest):
    return create_task(task)


@router.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks_route():
    return get_all_tasks()


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_single_task_route(task_id: int):
    return get_single_task(task_id)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_route(task_id: int, task: UpdateTaskRequest):
    return update_single_task(task_id, task)


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task_route(task_id: int):
    return delete_single_task(task_id)


@router.post("/task/suggest", status_code=201, response_model=TaskSuggestion)
def generate_task_suggstion(task: TaskSuggestionRequest):
    return task_suggestion(task)
