# import asyncio
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from loguru import logger

health_router = APIRouter(tags=["health"])


@health_router.get("/health/live", include_in_schema=False)
async def liveness_check() -> dict[str, str]:
    return {"status": "ok"}


@health_router.get("/health/ready", include_in_schema=False)
async def readiness_check() -> JSONResponse:
    try:
        # await asyncio.wait_for(check_db(), timeout=2)
        pass
    except Exception:
        logger.exception("Readiness check failed")
        return JSONResponse({"status": "not_ready"}, status_code=503)

    return JSONResponse({"status": "ready"})
