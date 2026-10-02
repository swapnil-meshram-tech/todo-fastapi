import logging

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

from app.core.exceptions.custom import AppError
from app.core.exceptions.responses import _error_response

logger = logging.getLogger(__name__)


async def app_error_handler(request: Request, exc: AppError):
    logger.warning(
        "%s %s - AppError: %s [%s]",
        request.method,
        request.url.path,
        exc.detail,
        exc.status_code,
    )

    return _error_response(exc.status_code, exc.detail)


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning(
        "%s %s - HttpError: %s [%s]",
        request.method,
        request.url.path,
        exc.detail,
        exc.status_code,
    )

    return _error_response(exc.status_code, exc.detail)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    safe_errors = jsonable_encoder(exc.errors())
    logger.warning(
        "%s %s - ValidationError: Input validation failed [422]",
        request.method,
        request.url.path,
    )

    return _error_response(422, "Input validation failed", errors=safe_errors)


async def global_exception_handler(request: Request, exc: Exception):
    # logger.exception("Unhandled: %s", exc)
    logger.exception(
        "%s %s - ServerError: %s [500]", request.method, request.url.path, exc
    )
    return _error_response(500, "Internal server error")
