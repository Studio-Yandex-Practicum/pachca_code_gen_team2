Генерация Клиента через openapi-python-client

Инструкция (работать в папке generator1):
1. В venv прописать

pip install openapi-python-client

2. Сгенерировать клиент командой

openapi-python-client generate --path openapi.yaml --custom-template-path=./templates --overwrite

3. Запустить скрипт-генератор

python script.py

4. Установить pachca-api-open-api-3-0-client в venv командой

pip install ./pachca-api-open-api-3-0-client

5. Запустить скрипт-пример запроса 

python pachca.py