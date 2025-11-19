import logging


# Best practice - add NullHandler to library's loggers.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def function():
    hh = logger.hasHandlers()
    hs = logger.handlers
    logger.debug(f"debug from {__name__}, {hh}, {hs}")
    logger.info(f"info from {__name__}, {hh}, {hs}")
    logger.warning(f"warning from {__name__}, {hh}, {hs}")
    logger.error(f"error from {__name__}, {hh}, {hs}")
    logger.critical(f"critical from {__name__}, {hh}, {hs}")
