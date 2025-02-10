import os
import subprocess
import sys

from generator1.generator import INSTALL_PATH

generator_script_path = os.path.join(INSTALL_PATH, "generator.py")


def generate():
    command = [sys.executable, generator_script_path, "generate"]
    result = subprocess.run(command, check=True, shell=True, text=True)

    if result.returncode == 0:
        print("Команда выполнена успешно.")
    else:
        print("Ошибка выполнения команды:", result.returncode)


def test():
    command = [sys.executable, generator_script_path, "test"]
    result = subprocess.run(command, check=True, shell=True, text=True)

    if result.returncode == 0:
        print("Команда выполнена успешно.")
    else:
        print("Ошибка выполнения команды:", result.returncode)


def gen_and_test():
    generate()
    test()
