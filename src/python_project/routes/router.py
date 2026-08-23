from fastapi import APIRouter

from .agent_routes import router as agent_router
from .chat_routes import router as chat_router
from .task_routes import router as task_router

router = APIRouter()

router.include_router(task_router)
router.include_router(chat_router)
router.include_router(agent_router)