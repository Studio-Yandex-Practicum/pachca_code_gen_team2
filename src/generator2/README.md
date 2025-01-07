Генерация Клиента через прямой код Python

Инструкция:

- Развернуть venv в корне директории
- Установить зависимости из requirements.txt
- Запустить выполнение файла request_methods_generator.py. В файл request_methods.py будут записаны методы запроса для класса Bot из файла bot.py

# Генерация моделей pydantic для requestBody эндпоинтов

Метод process_endpoints в yaml_processor.py позволяет создать модели pydantic для каждого эндпоинта
Метод возвращает кортеж из двух список - path query параметров эндпоинта
Метод записывает (пока что в консоль) модели pydantic.