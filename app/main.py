import logging
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

from app.core.exceptions.custom import AppError
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.exceptions.handlers import (
    app_error_handler,
    http_exception_handler,
    validation_exception_handler,
    global_exception_handler,
)
from app.db.database import init_db
from app.routers.health import health_router
from app.routers.todo import todo_router
from app.schemas.responses import MessageResponse


setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(App: FastAPI) -> AsyncGenerator[None]:
    await init_db()
    logger.info("Database initialized")

    yield

    # await close_db()
    # logger.info("Database connection closed")


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, version="1.0.0", lifespan=lifespan)

    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

    app.include_router(health_router)
    app.include_router(todo_router)

    
    @app.get("/")
    async def home():
        return {"message": "server is running"}

    return app


app = create_app()
