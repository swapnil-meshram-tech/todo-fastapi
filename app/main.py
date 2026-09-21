from fastapi import FastAPI, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

from app.exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
    global_exception_handler,
)

from app.routers.todo import todo_router
from app.schemas.responses import MessageResponse

app = FastAPI()


app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


app.include_router(todo_router)


@app.get(
    "/",
    response_model=MessageResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def home():
    return MessageResponse(message="Server is running")
