from .tasks_tools import (
    create_task_tool,
    delete_task_tool,
    get_tasks_tool,
    update_task_tool,
)

tool_registry = {
    "create_task" : create_task_tool,
    "get_tasks" : get_tasks_tool,
    "update_task": update_task_tool,
    "delete_task": delete_task_tool
}