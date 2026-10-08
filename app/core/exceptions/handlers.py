from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.exceptions.custom import AppError
from app.core.exceptions.responses import _error_response


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    logger.warning(
        "{} {} - AppError: {} [{}]",
        request.method,
        request.url.path,
        exc.detail,
        exc.status_code,
    )

    return _error_response(exc.status_code, exc.detail)


async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:
    logger.warning(
        "{} {} - HttpError: {} [{}]",
        request.method,
        request.url.path,
        exc.detail,
        exc.status_code,
    )

    return _error_response(exc.status_code, exc.detail, exc.headers)


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    json_errors = jsonable_encoder(exc.errors())
    logger.warning(
        "{} {} - ValidationError: Input validation failed [422]",
        request.method,
        request.url.path,
    )

    return _error_response(422, "Input validation failed", errors=json_errors)


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception(
        "{} {} - ServerError: {} [500]", request.method, request.url.path, exc
    )

    return _error_response(500, "Internal server error")
