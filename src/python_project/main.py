from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .routes.router import router
from .store.exception import ConversationNotFoundEror

load_dotenv()
app = FastAPI()

app.include_router(router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,    
        content={
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
            }
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": 422,
                "message": "Request validation failed",
                "details": exc.errors(),
            }
        }
    )

@app.exception_handler(ConversationNotFoundEror)
async def conversation_not_found_handler(request: Request, exc: ConversationNotFoundEror):
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": 404,
                "message": str(exc)
            }
        }
    )