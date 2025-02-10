import json
import os
from pathlib import Path

from dotenv import load_dotenv
from setuptools import find_packages, setup

PACKAGE_VERSION = 'Версия из YAML'

load_dotenv()

this_directory = Path(__file__).parent
long_description = (
    this_directory / "../../README.md"
).read_text(encoding='utf-8')


def read_pipenv_dependencies(fname):
    """Получаем из Pipfile.lock зависимости по умолчанию."""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]


if __name__ == '__main__':
    setup(
        name='PachcaAPI',
        long_description=long_description,
        long_description_content_type='text/markdown',
        version=os.getenv('PACKAGE_VERSION', PACKAGE_VERSION),
        package_dir={'': '..'},
        packages=find_packages('..', include=[
                'generator1*']),
        include_package_data=True,
        description='A pachca_api package generator1.',
        install_requires=[
            *read_pipenv_dependencies('Pipfile.lock'),
        ],
        entry_points={
            'console_scripts': [
                'run_generate_and_test=generator1.api_generator:gen_and_test',
                'run_generator=generator1.api_generator:ganerate',
                'run_test=generator1.api_generator:test',
            ],
        },
    )
