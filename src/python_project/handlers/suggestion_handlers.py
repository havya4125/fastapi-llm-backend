from ..services.claude_service import generate_task_suggestion
from ..utils import append_user_message


# Handler for generating task suggestion
def task_suggestion(task):
    messages = []
    append_user_message(messages, task.message)
    response = generate_task_suggestion(messages)
    return response
