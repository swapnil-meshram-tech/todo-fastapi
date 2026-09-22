from pydantic import BaseModel


class MessageResponse[T](BaseModel):
    status: str = "success"
    message: str
    data: T | None = None


class ErrorResponse[T](BaseModel):
    status: str = "error"
    detail: str
    errors: T | None = None
