import logging

from constants import LOG_FILE_NAME


def setup_logging(logger_name: str) -> logging.Logger:
    logging.basicConfig(encoding='utf-8')
    logger = logging.getLogger(logger_name)
    logger
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(LOG_FILE_NAME)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
