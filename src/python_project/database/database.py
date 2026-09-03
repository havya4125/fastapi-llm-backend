import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Task

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
        title = "Learn about SQLalchemy",
        description = "Understand sessions and models",
        priority = "high"
    )

    session.add(task)
    session.commit()

    print(task.id)