from fastapi import FastAPI, status
from app.routers.todo import todo_router
from app.schemas.response import MessageResponse

app = FastAPI()
app.include_router(todo_router)


@app.get(
    "/",
    response_model=MessageResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def home():
    return MessageResponse(message="Server is running")
