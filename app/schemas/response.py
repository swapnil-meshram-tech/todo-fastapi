from pydantic import BaseModel


class MessageResponse[T](BaseModel):
    status: str | None = None
    message: str | None = None
    error: str | None = None
    data: T | None = None
