from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # logger.debug("DEBUG - cyan")
    # logger.info("INFO - green")
    # logger.warning("WARNING - yellow")
    # logger.error("ERROR - red")

    try:
        init_db()
        yield

    finally:
        pass
        # await close_db()
