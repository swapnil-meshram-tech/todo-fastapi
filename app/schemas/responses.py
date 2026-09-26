from pydantic import BaseModel
from typing import Literal


class MessageResponse[T](BaseModel):
    status: str = "success"
    message: str
    data: T | None = None


class ErrorResponse[T](BaseModel):
    status: Literal["error"] = "error"
    detail: str
    errors: T | None = None
