from ..handlers.tasks_handlers import create_task
from ..schemas.task import CreateTaskRequest


def create_task_tool(title: str, priority: str, description: str | None = None):
    task = CreateTaskRequest(
        title=title,
        priority=priority,
        description=description
    )
    return create_task(task)