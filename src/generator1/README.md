Генерация Клиента через openapi-python-client

Инструкция (работать в папке generator1):
1. В venv прописать

pip install -r requirements.txt

2. Изменить константу INSTALL_PATH в generator.py и ее импорты в pydantic_script.py и script.py в зависимости от запуска генеротора и тестов локально или для создания библиотеки (описание в комментариях)

3. Сгенерировать клиент командой

python generator.py generate

2.1 По желанию можно указать именованный аргумент --url,  
с указанием ссылки на спецификацию, по которой будет происходить генерация клиента.  
Если не указывать, то будет взята официальная спецификация от Пачки по адресу:  
https://raw.githubusercontent.com/pachca/openapi/main/openapi.yaml

python generator.py generate --url *ссылка на YAML спецификацию*

4. Запустить скрипт-пример запроса 

python generator.py test
