import asyncio
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from loguru import logger

health_router = APIRouter(tags=["health"])


@health_router.get("/health")
async def health_check():
    return {"status": "ok"}


@health_router.get("/ready")
async def readiness_check():
    try:
        # await asyncio.wait_for(check_db(), timeout=2)
        return {"status": "ready"}
    except TimeoutError:
        # logger.warning("Readiness check timeout.")
        return JSONResponse({"status": "not_ready"}, status_code=503)
    except Exception as e:
        # logger.warning("Readiness check failed: %s", e)
        return JSONResponse({"status": "not_ready"}, status_code=503)
