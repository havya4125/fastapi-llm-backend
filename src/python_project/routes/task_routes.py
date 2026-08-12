from fastapi import APIRouter
from ..schemas.task import CreateTaskRequest, UpdateTaskRequest
from ..handlers.tasks_handlers import create_task, get_all_tasks, get_single_task, update_single_task, delete_single_task

router = APIRouter()

@router.post('/tasks')
def create_task_route(task: CreateTaskRequest):
    return create_task(task)

@router.get('/tasks')
def get_all_tasks_route():
    return get_all_tasks()

@router.get('/tasks/{task_id}')
def get_single_task_route(task_id : int):
    return get_single_task(task_id)

@router.put('/tasks/{task_id}')
def update_task_route(task_id: int, task: UpdateTaskRequest):
    return update_single_task(task_id, task)

@router.delete('/tasks/{task_id}')
def delete_task_route(task_id: int):
    return delete_single_task(task_id)