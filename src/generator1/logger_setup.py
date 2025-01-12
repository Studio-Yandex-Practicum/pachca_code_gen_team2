import logging


def setup_logging(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('client_generator.log', encoding='utf-8')
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
