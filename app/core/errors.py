from fastapi.responses import JSONResponse
from typing import Any
from app.core.responses import ErrorResponse


# def error_response(status_code: int, detail: str, errors: Any | None = None):
#     content = {"status": "error", "detail": detail}
#     if errors is not None:
#         content["errors"] = errors
#     return JSONResponse(status_code=status_code, content=content)


def error_response(status_code: int, detail: str, errors: Any | None = None):
    body = ErrorResponse(detail=detail, errors=errors)
    return JSONResponse(
        status_code=status_code, content=body.model_dump(exclude_none=True)
    )
