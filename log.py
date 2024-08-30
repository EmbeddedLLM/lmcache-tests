import logging
from logging import Logger

#logging.basicConfig(
#        format='\033[33m%(levelname)s: \033[0m%(message)s [%(asctime)s.%(msecs)03d]', 
#        level=logging.INFO,
#    )

def build_format(color):
    reset = "\x1b[0m"
    underline = "\x1b[3m"
    return f"{color}[%(asctime)s] %(levelname)s:{reset} %(message)s {underline}(%(filename)s:%(lineno)d:%(name)s){reset}"

class CustomFormatter(logging.Formatter):

    grey = "\x1b[1m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: build_format(grey),
        logging.INFO: build_format(green),
        logging.WARNING: build_format(yellow),
        logging.ERROR: build_format(red),
        logging.CRITICAL: build_format(bold_red),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def init_logger(name: str) -> Logger:
    logger = logging.getLogger(name)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)

    return logger

if __name__ == "__main__":
    logger = init_logger(__name__)
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")