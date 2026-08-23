from ..handlers.tasks_handlers import (
    create_task,
    delete_single_task,
    get_all_tasks,
    update_single_task,
)
from ..schemas.task import CreateTaskRequest, UpdateTaskRequest


def create_task_tool(title: str, priority: str, description: str | None = None):
    task = CreateTaskRequest(
        title=title,
        priority=priority,
        description=description
    )
    return create_task(task)

def get_tasks_tool():
    return get_all_tasks()

def update_task_tool(title: str, description: str, priority: str, completed: bool, task_id: int):
    task = UpdateTaskRequest(
        title=title,
        description=description,
        priority=priority,
        completed=completed
    )
    return update_single_task(task_id, task)

def delete_task_tool(task_id: int):
    return delete_single_task(task_id)