from fastapi import APIRouter
from app.core.responses import MessageResponse

todo_router = APIRouter(prefix="/todo", tags=["Todo"])


@todo_router.get("/")
async def get_todos():
    return MessageResponse(message="get", data="data")
