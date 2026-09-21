from fastapi import Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.responses.errors import error_response


async def http_exception_handler(request: Request, exe: StarletteHTTPException):
    return error_response(exe.status_code, exe.detail)


async def validation_exception_handler(request: Request, exe: RequestValidationError):
    return error_response(422, "Validation error", errors=exe.errors())


async def global_exception_handler(request: Request, exe: Exception):
    return error_response(500, "Internal server error")
