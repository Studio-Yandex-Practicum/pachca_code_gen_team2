import os.path
import subprocess
import sys
import os
import requests


MIN_ARGS = 2
COMMAND_INDEX = 1
GENERATE_COMMAND = "generate"
INSTALL_TEST_COMMAND = "test"
DEFAULT_YAML_URL = (
    "https://raw.githubusercontent.com/pachca/openapi/main/openapi.yaml"
)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPENAPI_FILE_PATH = os.path.join(BASE_DIR, "openapi.yaml")


def run_command(command):
    """Функция для выполнения команды в терминале."""
    try:
        subprocess.run(command, check=True, shell=True, text=True)
        print(f"Команда выполнена: {command}")
    except subprocess.CalledProcessError as e:
        print(
            f"Ошибка при выполнении команды: {command}\n"
            f"Код ошибки: {e.returncode}\n"
            f"Вывод:\n{e.stderr}"
        )


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
    run_command(
        f"openapi-python-client generate --path {OPENAPI_FILE_PATH} "
        f"--custom-template-path=./templates --overwrite"
    )
    run_command("python script.py")


def install_and_run_tests():
    """Установка пакета и запуск тест-запросов."""
    print("Установка пакета и запуск тест-запросов...")
    run_command("pip install ./pachca-api-open-api-3-0-client")
    run_command("python pachca.py")


if __name__ == "__main__":
    if len(sys.argv) < MIN_ARGS:
        print(
            "Пример команды: python generator.py [generate|test] "
            "[--url <ссылка на .yaml>]"
        )
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
        print(
            "Некорректный аргумент. Введите 'generate' для генерации клиента "
            "или 'test' для запуска тестов."
        )
        sys.exit(COMMAND_INDEX)
