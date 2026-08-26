import logging
from io import StringIO


def make_logger(name: str, level: int, stream: StringIO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
    logger.addHandler(handler)
    return logger


def audit(logger: logging.Logger, event: str, ok: bool) -> None:
    if ok:
        logger.info("OK: %s", event)
    else:
        logger.error("FAILED: %s", event)
