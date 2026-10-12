import asyncio
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from loguru import logger

health_router = APIRouter(tags=["health"])


@health_router.get("/health/live")
async def liveness_check() -> dict[str, str]:
    return {"status": "ok"}


@health_router.get("/health/ready")
async def readiness_check() -> JSONResponse:

    # checks = {}

    try:
        # await asyncio.wait_for(check_db(), timeout=2)
        # checks["db"] = "ok"

        return JSONResponse({"status": "ready"})

    except TimeoutError as t:
        logger.warning("Readiness error: timed out")
        return JSONResponse(
            {"status": "not_ready", "detail": type(t).__name__}, status_code=503
        )

    except Exception as e:  # noqa
        logger.exception("Readiness error: {} - {}", type(e).__name__, e)
        return JSONResponse(
            {"status": "not_ready", "detail": type(e).__name__}, status_code=503
        )
