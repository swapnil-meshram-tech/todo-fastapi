from pydantic import BaseModel


class MessageResponse[T](BaseModel):
    status: str = "success"
    message: str | None = None
    data: T | None = None
