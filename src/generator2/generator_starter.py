import os
import subprocess

from logger_setup import setup_logging
from request_methods_generator import generate
from yaml_processor import process_endpoints


def generate_client():
    logger = setup_logging('client_generator')

    try:
        process_endpoints()
    except Exception as ex:
        logger.critical('Не удалось создать модели pydantic! '
                        f'Возникла ошибка: {ex}')

    try:
        generate()
    except Exception as ex:
        logger.critical('Не удалось создать эндпоинты! '
                        f'Возникла ошибка: {ex}')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger.debug(f'Рабочая директория: {dir_path}')
    try:
        subprocess.run(
            ['black', f'{dir_path}/models', '--line-length', '79'], check=True
        )
        subprocess.run(
            ['black', f'{dir_path}/request_methods.py', '-l', '79'], check=True
        )
        logger.debug('Форматирование сгенерированного кода завершено!')
    except Exception as ex:
        logger.error(f'Не удалось провести форматирование кода: {ex}')


if __name__ == '__main__':
    generate_client()
