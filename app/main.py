from contextlib import asynccontextmanager

from fastapi import FastAPI, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

from app.db.database import init_db
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.handlers import (
    http_exception_handler,
    validation_exception_handler,
    global_exception_handler,
)
from app.routers.todo import todo_router
from app.schemas.responses import MessageResponse


setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title=settings.APP_NAME, version="1.0.0", lifespan=lifespan)


app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


app.include_router(todo_router)


@app.get(
    "/",
    response_model=MessageResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def home():
    return MessageResponse(message="server is running")


@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}
