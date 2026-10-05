from fastapi.responses import JSONResponse


def _error_response(
    status_code: int, detail: str, errors: list[dict] | None = None
) -> JSONResponse:
    body = {"detail": detail}
    if errors is not None:
        body["errors"] = errors
    return JSONResponse(status_code=status_code, content=body)
