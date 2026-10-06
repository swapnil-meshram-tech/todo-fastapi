from loguru import logger
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from starlette.middleware.gzip import GZipMiddleware

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


setup_logging(level=settings.log_level, json_logs=settings.json_logs)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    await init_db()
    logger.info("Database initialized")
    yield

    # await close_db()
    # logger.info("Database connection closed")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="1.0.0",
        debug=settings.debug,
        lifespan=lifespan,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        openapi_url="/openapi.json" if settings.debug else None,
    )

    app.add_middleware(GZipMiddleware, minimum_size=1000)

    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

    app.include_router(health_router)
    app.include_router(todo_router, prefix="/api/v1")

    @app.get("/")
    async def home():
        return {"message": "server is running"}

    return app


app = create_app()
