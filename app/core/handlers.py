from fastapi import Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
import logging
from app.core.errors import error_response


logger = logging.getLogger(__name__)


async def app_error_handler(status_code, detail):
    return error_response(status_code, detail)


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return error_response(exc.status_code, exc.detail)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return error_response(422, "Validation error", errors=exc.errors())


async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled: %s", exc)
    return error_response(500, "Internal server error")
