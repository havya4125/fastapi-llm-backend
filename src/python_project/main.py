from fastapi import FastAPI

from .routes.task_routes import router

app = FastAPI()

app.include_router(router)
