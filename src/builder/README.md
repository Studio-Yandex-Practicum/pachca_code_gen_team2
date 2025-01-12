# Инструменты для генерации библиотеки


## Порядок подготоительных действий:

1. pip install pipenv

2. pipenv install requirements.txt

- pipenv считал всю инфу с venv и создал файлы зависимостей Pipfile (в том числе lock)

## Создать версию библиотеки при помощи команды (пример):
- export PACKAGE_VERSION='1.1.0'

## Запуск создания библиотеки при помощи команды:

- make build

## Распаковка бибилотеки (для Windows)
- python -m venv venv
- source venv/Scripts/activate
- pip install <имя файла>.whl
