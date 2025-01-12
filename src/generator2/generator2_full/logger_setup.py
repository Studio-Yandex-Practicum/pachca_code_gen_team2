import logging
from logging.handlers import RotatingFileHandler

from .constants import BACKUP_COUNT, LOG_FILE_NAME, MAX_FILE_SIZE


def setup_logging(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    file_handler = RotatingFileHandler(
        LOG_FILE_NAME, maxBytes=MAX_FILE_SIZE,
        backupCount=BACKUP_COUNT,
        encoding='utf-8'
    )
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
