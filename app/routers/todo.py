from fastapi import APIRouter
from app.schemas.responses import MessageResponse

todo_router = APIRouter(prefix="/todo", tags=["Todo"])


@todo_router.get("/")
def get_todos():
    return MessageResponse(message="get", data="data")
