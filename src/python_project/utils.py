def append_user_message(messages, message):
    user_message = {
        "role" : "user",
        "content" : message
    }
    messages.append(user_message)

def append_assistant_message(messages, message):
    assistant_message = {
        "role" : "assistant",
        "content" : message
    }
    messages.append(assistant_message)