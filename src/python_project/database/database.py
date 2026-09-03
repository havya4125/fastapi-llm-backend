import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..repositories.task_repository import TaskRepository
from .models import Task

repository = TaskRepository()

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")


engine = create_engine(DATABASE_URL)

# Factory for creating sessions
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

with SessionLocal() as session:
    task = Task(
        title = "Learn about node.js",
        description = "Learn abouut stream mainly",
        priority = "high",

    )
    created_task = repository.create(session, task)

    if created_task:
        print(created_task.id)
        print(created_task.title)
    else:
        print("Task not found")