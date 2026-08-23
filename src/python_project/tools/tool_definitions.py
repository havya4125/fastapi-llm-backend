task_tools = [
    {
        "name": "create_task",
        "description": "Create a new task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title of the task."
                },
                "priority": {
                    "type": "string",
                    "description": "The priority of the task."
                },
                "description": {
                    "type": "string",
                    "description": "An optional description of the task."
                }
            },
            "required": ["title", "priority"]
        }
    },
    {
        "name": "get_tasks",
        "description": "Get all tasks.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "update_task",
        "description": "Update an existing task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "The ID of the task to update."
                },
                "title": {
                    "type": "string",
                    "description": "The updated title of the task."
                },
                "description": {
                    "type": "string",
                    "description": "The updated description of the task."
                },
                "priority": {
                    "type": "string",
                    "description": "The updated priority of the task."
                },
                "completed": {
                    "type": "boolean",
                    "description": "Whether the task is completed."
                }
            },
            "required": [
                "task_id",
                "title",
                "description",
                "priority",
                "completed"
            ]
        }
    },
    {
        "name": "delete_task",
        "description": "Delete an existing task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "The ID of the task to delete."
                }
            },
            "required": ["task_id"]
        }
    }
]