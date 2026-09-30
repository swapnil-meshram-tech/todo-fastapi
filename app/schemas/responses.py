from pydantic import BaseModel


class MessageResponse[T](BaseModel):
    message: str
    data: T | None = None


class FieldError(BaseModel):
    field: str
    message: str


class ErrorResponse(BaseModel):
    detail: str
    errors: list[dict] | None = None
