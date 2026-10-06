import sys
import logging
from loguru import logger


def setup_logging(level: str = "INFO", json_logs: bool = False):
    logger.remove()

    if json_logs:
        logger.add(sys.stdout, level=level, serialize=True)
    else:
        logger.add(
            sys.stdout,
            level=level,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        )

    # to log only error, not info
    # logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
