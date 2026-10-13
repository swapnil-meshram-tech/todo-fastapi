from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.gzip import GZipMiddleware

from app.core.config import settings
from app.core.exceptions.custom import AppError
from app.core.exceptions.handlers import (
    app_exception_handler,
    global_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from app.core.lifespan import lifespan
from app.core.logging import setup_logging
from app.routers.health import health_router
from app.routers.todo import todo_router


setup_logging(level=settings.log_level, json_logs=settings.json_logs)


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        lifespan=lifespan,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        openapi_url="/openapi.json" if settings.debug else None,
    )

    app.add_middleware(GZipMiddleware, minimum_size=1000)

    app.add_exception_handler(AppError, app_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

    app.include_router(health_router)
    app.include_router(todo_router, prefix="/api/v1")

    @app.get("/", include_in_schema=False)
    async def root() -> dict[str, str]:
        return {"message": "Server is running"}

    return app


app = create_app()
