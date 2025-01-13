from setuptools import setup, find_packages

import json
import os
from dotenv import load_dotenv
from pathlib import Path


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
        name='pachca_generator2',
        long_description=long_description,
        long_description_content_type='text/markdown',
        version=os.getenv('PACKAGE_VERSION', PACKAGE_VERSION),
        package_dir={'': '../generator2'},
        packages=find_packages(
            '../generator2', include=[
                'generator2_full*']
        ),
        description='A pachca_api package generator2.',
        install_requires=[
              *read_pipenv_dependencies('Pipfile.lock'),
        ],
        python_version='>=3.11'
    )
