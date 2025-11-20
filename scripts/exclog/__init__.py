import logging
import sys


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def log_exception(*exc_info):
    logger.error("Uncaught exception:", exc_info=exc_info, stack_info=True)
    sys.__excepthook__(*exc_info)


def enable():
    sys.excepthook = log_exception


if __name__ == "__main__":
    logger.handlers = []
    enable()
    result = 1 / 0
