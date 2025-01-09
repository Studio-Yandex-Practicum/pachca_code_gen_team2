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
        logger.critical('Unable to create pydantic models! '
                        f'Error: {ex}')

    try:
        generate()
    except Exception as ex:
        logger.critical('Unable to create endpoints! '
                        f'Error: {ex}')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger.debug(f'Working directory: {dir_path}')
    try:
        subprocess.run(
            ['black', f'{dir_path}/models', '--line-length', '79'], check=True
        )
        subprocess.run(
            ['black', f'{dir_path}/request_methods.py', '-l', '79'], check=True
        )
        logger.debug('Finished code formatting!')
    except Exception as ex:
        logger.error(f'Unable to format code: {ex}')


if __name__ == '__main__':
    generate_client()
