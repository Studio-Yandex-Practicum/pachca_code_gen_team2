import os
import os.path
import site
import subprocess
import sys

import requests

INSTALL_PATH = os.path.join(site.getsitepackages()[1], "generator1")
# INSTALL_PATH = ".generator1"
MIN_ARGS = 2
COMMAND_INDEX = 1
GENERATE_COMMAND = "generate"
INSTALL_TEST_COMMAND = "test"
DEFAULT_YAML_URL = "https://raw.githubusercontent.com/pachca/openapi/main/openapi.yaml"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPENAPI_FILE_PATH = os.path.join(BASE_DIR, "openapi.yaml")


def run_command(command):
    """Функция для выполнения команды в терминале."""
    try:
        subprocess.run(command, check=True, shell=True, text=True)
        print(f"Команда выполнена: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {command}\nКод ошибки: {e.returncode}\nВывод:\n{e.stderr}")


def download_yaml(url):
    """Загрузка YAML файла по URL и сохранение в нужную директорию."""
    print(f"Загрузка YAML файла с {url}...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        os.makedirs(os.path.dirname(OPENAPI_FILE_PATH), exist_ok=True)
        with open(OPENAPI_FILE_PATH, "wb") as file:
            file.write(response.content)
        print(f"Файл сохранён тут: {OPENAPI_FILE_PATH}")
    except requests.RequestException as e:
        print(f"Ошибка при загрузке YAML файла: {e}")
        sys.exit(1)


def generate_client(yaml_url):
    """Генерация клиента и запуск скрипта-генератора."""
    download_yaml(yaml_url)
    print("Генерация клиента...")
    openapi_python_client = (
        f"openapi-python-client generate --path {OPENAPI_FILE_PATH} "
        f"--custom-template-path={INSTALL_PATH}/templates --overwrite "
        f"--output-path {INSTALL_PATH}"
    )
    run_command(openapi_python_client)

    pydantic_script_path = os.path.join(INSTALL_PATH, "pydantic_script.py")
    script_path = os.path.join(INSTALL_PATH, "script.py")
    run_command([sys.executable, pydantic_script_path])
    run_command([sys.executable, script_path])


def install_and_run_tests():
    """Установка пакета и запуск тест-запросов."""
    pachca_path = os.path.join(INSTALL_PATH, "pachca.py")
    print("Установка пакета и запуск тест-запросов...")
    run_command(f"pip install {INSTALL_PATH}")
    run_command([sys.executable, pachca_path])


if __name__ == "__main__":
    if len(sys.argv) < MIN_ARGS:
        print("Пример команды: python generator.py [generate|test] [--url <ссылка на .yaml>]")
        sys.exit(COMMAND_INDEX)

    command = sys.argv[COMMAND_INDEX]
    yaml_url = DEFAULT_YAML_URL
    if "--url" in sys.argv:
        url_index = sys.argv.index("--url") + 1
        if url_index < len(sys.argv):
            yaml_url = sys.argv[url_index]
        else:
            print("Ошибка: не указан url после --url")
            sys.exit(1)
    commands = {
        GENERATE_COMMAND: lambda: generate_client(yaml_url),
        INSTALL_TEST_COMMAND: install_and_run_tests,
    }
    if command in commands:
        commands[command]()
    else:
        print("Некорректный аргумент. Введите 'generate' для генерации клиента или 'test' для запуска тестов.")
        sys.exit(COMMAND_INDEX)
