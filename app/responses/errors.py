from fastapi.responses import JSONResponse
from typing import Any


def error_response(status_code: int, message: str, errors: Any | None = None):
    content = {"status": "error", "message": message}
    if errors is not None:
        content["errors"] = errors
    return JSONResponse(status_code=status_code, content=content)
