from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database.models import Task


class TaskRepository:
    
    def get_all(self, session: Session):
        statement = select(Task)
        result = session.execute(statement)

        return result.scalars().all()
    
    def get_by_id(self, session: Session, task_id : int):
        statement = select(Task).where(Task.id == task_id)
        result = session.execute(statement)
        return result.scalar_one_or_none()
    
    def create(self, session: Session, task: Task):
        session.add(task)
        session.commit()
        session.refresh(task)

        return task