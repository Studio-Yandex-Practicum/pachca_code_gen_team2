Инструкция (работать в папке generator2 при активированном venv):

1. Установить зависимости

pip install -r requirements.txt

2. Запустить генерацию схем

python yaml_processor.py

3. Запустить генерацию эндпоинтов

python request_methods_generator.py

4. Запустить скрипт-пример запроса

python pachca.py
