import sys
import logging

from loguru import logger


def setup_logging(level: str, json_logs: bool):
    logger.remove()

    if json_logs:
        logger.add(
            sys.stderr,
            level=level,
            serialize=True,
            backtrace=False,
            diagnose=False,
            enqueue=True,
        )

    else:
        logger.add(
            sys.stderr,
            level=level,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            # format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            backtrace=False,
            diagnose=False,
            enqueue=True,
        )

    # to log only error, not info
    # logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
