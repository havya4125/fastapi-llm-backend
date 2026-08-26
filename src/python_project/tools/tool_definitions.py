task_tools = [
    {
        "name": "create_task",
        "description": (
            "Create a new task when the user asks to add, create, or track a new task."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title or name of the task.",
                },
                "priority": {
                    "type": "string",
                    "description": (
                        "The priority of the task. Must be one of: low, medium, or high."
                    ),
                },
                "description": {
                    "type": "string",
                    "description": "An optional description explaining what the task is about.",
                },
            },
            "required": ["title", "priority"],
        },
    },
    {
        "name": "get_tasks",
        "description": (
            "Retrieve the user's existing tasks when they ask to "
            "view, list, show, or check their tasks."
        ),
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "update_task",
        "description": (
            "Update one or more fields of an existing task. "
            "Use this when the user wants to change a task's "
            "title, description, priority, or completion status."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "The ID of the task to update.",
                },
                "title": {
                    "type": "string",
                    "description": "The new title of the task.",
                },
                "description": {
                    "type": "string",
                    "description": "The new description of the task.",
                },
                "priority": {
                    "type": "string",
                    "description": "The new priority of the task. Must be one of: low, medium, or high.",
                },
                "completed": {
                    "type": "boolean",
                    "description": (
                        "Whether the task should be marked as completed. "
                        "Use true to complete it and false to mark it incomplete."
                    ),
                },
            },
            "required": ["task_id"],
        },
    },
    {
        "name": "delete_task",
        "description": (
            "Delete an existing task when the user explicitly asks "
            "to remove or delete it."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "The ID of the task to delete.",
                }
            },
            "required": ["task_id"],
        },
    },
]
