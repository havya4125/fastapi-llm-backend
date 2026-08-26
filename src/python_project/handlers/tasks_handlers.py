from ..exceptions.task_exceptions import TaskNotFoundError

tasks = []


# Handler for creating tasks
def create_task(task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "completed": False,
    }
    tasks.append(new_task)
    return new_task


# Handler fot get all tasks
def get_all_tasks():
    return tasks


# Handler for get single task
def get_single_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise TaskNotFoundError(f"No task is present with id {task_id}")


# Handler for update task
def update_single_task(task_id, task):
    for index, t in enumerate(tasks):
        if t["id"] == task_id:
            updates = task.model_dump(exclude_none = True)
            t.update(updates)
            tasks[index] = t
            return t
    raise TaskNotFoundError(f"No task is present with id {task_id}")


# Handler for delete task
def delete_single_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise TaskNotFoundError(f"No task found with id {task_id}")
