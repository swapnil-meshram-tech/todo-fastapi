from fastapi.responses import JSONResponse


def _error_response(
    status_code: int, detail: str, errors: list[dict] | None = None, headers: str
) -> JSONResponse:
    body = {"detail": detail}
    if errors is not None:
        body["errors"] = errors
    if headers is not None:
        body["headers"] = headers
    return JSONResponse(status_code=status_code, content=body)
