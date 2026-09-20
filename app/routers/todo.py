from fastapi import APIRouter
from app.schemas.response import MessageResponse

todo_router = APIRouter(prefix="/todo", tags=["Todo"])


@todo_router.get("/")
async def get_todos():
    return MessageResponse(status="success", message="get", data="data")
