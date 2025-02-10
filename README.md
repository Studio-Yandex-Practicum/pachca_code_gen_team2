# Парсер OpenAPI для мессенджера "Пачка"

### Библиотека для работы с API мессенджера "Пачка", автоматически генерируемая на Python. 🐍

## 🔖 Цели и задачи проекта

Основная цель проекта — создание инструмента для преобразования спецификации OpenAPI в Python-пакет. 📋  
Этот пакет предоставляет структурированный и удобный интерфейс для взаимодействия с открытым API мессенджера "Пачка". 🌐

### ✅ Проект включает:  
- **Конвертацию файлов OpenAPI**: Автоматизация генерации Python-кода, содержащего методы и классы для работы с API.  
- **Подготовку Python-пакета**: Упаковка сгенерированного кода для распространения через менеджеры пакетов, такие как pip и poetry.

### 🔧 Основные функции:
- **Обработка HTTP-запросов**: Сгенерированный код выполняет авторизованные запросы к серверу с использованием токенов.
- **Структуры данных**: Входные и выходные данные представлены в виде Python-классов.  
- **Методы для эндпоинтов**: Методы названы в соответствии с эндпоинтами API, что обеспечивает ясность и соответствие.  
- **Полная документация**: Сгенерированные классы и методы включают подробные docstring’и, созданные на основе OpenAPI.

---

## 📜 Детали реализации

### 📄 Подготовка OpenAPI-файла:
- Формат: JSON или YAML.  
- Версия OpenAPI: 3.0.  

**Обязательные секции:**  
- `openapi`: Версия файла OpenAPI.  
- `info`: Общая информация об API.  
- `servers`: Данные о серверах для выполнения запросов.  
- `paths`: Описание эндпоинтов с параметрами `operationId` и `tags` для генерации методов.  
- `components`: Схемы данных для структур входных и выходных параметров.

## 💡 Команда написания спецификации  

- [Денис Лопин](https://github.com/fantyissues)
- [Александр Аполинаров](https://github.com/Alexander-Klp)
- [Александр Тогузов](https://github.com/Imuntouchable)

### 🔨 Генерация кода:
- **Основной объект**: Центральный класс (`Pachca` - для 1 генератора, `Bot` - для 2 генератора), инициализируемый токеном авторизации. 
- **Методы эндпоинтов**: Генерируются на основе параметра `operationId` из OpenAPI.  
- **Модели данных**: Определены с использованием `pydantic` для входных и выходных схем.  
- **Обработка ошибок**: Пользовательские исключения для API-ошибок на основе описания OpenAPI.

---

# 🔧 ***generator1***

### 📚 Используемый стек и технологии:
- **Python 3.12+**.
- **httpx (0.28.1)**: Для выполнения асинхронных HTTP-запросов.  
- **Jinja2 (3.1.4)**: Для генерации кода на основе шаблонов.  
- **ruamel.yaml (0.18.6)**: Для работы с YAML файлами.  
- **openapi-python-client (0.22.0)**: Для автоматической генерации клиентского кода на основе OpenAPI спецификаций.

## 📂 Структура генератора

### 🛠️ Основные компоненты
_src/generator1/_

#### 🛠️ pachca-api-open-api-3-0-client/client.py
- Автоматически генерируемый файл (появляется после запуска генерации)
- Представлена моделями и методами для работы с API на основе OpenAPI спецификации
- Содержит "динамическую" часть (основной класс для работы с API) после запуска скрипта-генератора
- Передает запрос пользователя в "статическую" часть, преобразовав из формата Python в JSON 
- Передает ответ пользователю от "статической" части, преобразовав из формата JSON в Python

#### 🧩 templates 
- Директория хранения основных шаблонов для автоматической генерации

#### 🔧 client_servis.py
- "Статическая" часть
- Отвечает за отправку/приемку данных на/от сервер(а)
- Полученные данные передает в "динамическую" часть (генерируемую)
- Содержит логику обеспечении безопасности и управления доступом

#### 💾 script.py
- Создает "динамическую" часть в client.py
- Собирает главный и основной класс Pachca для работы с API

#### 📜 requirements.txt
- Список зависимостей генератора с версиями

#### 🧪 pachca.py
- Пример использования сгенерированного API клиента
- Тестовые вызовы различных методов API

#### 📄 openapi.yaml:
- OpenAPI спецификации API
- Описание эндпоинтов, схем, параметров

#### 📁 pachca-api-open-api-3-0-client/
- директория автоматически сгенерированного кода

---

## 🚀 Установка и использование

### 🛠️ Инструкция (работать в папке `generator1` при активированном `venv`):
1. **Создайте файл `.env`** в директории `generator1`, с токеном для работы с API "Пачка".  
Пример файла:  
    ```
    TOKEN=ваштокен
    ```
2. **Создайте и активируйте виртуальное окружение, установите зависимости**:  
    - Для Linux/gitBash:
        ```bash
        python3 -m venv venv  
        source venv/scripts/activate  
        pip install -r requirements.txt  
        ```  
    - Для Windows cmd: 
        ```bash
        python -m venv venv  
        .\venv\scripts\activate  
        pip install -r requirements.txt  
        ```  
3. **Запустите генерацию клиента:**:  
    ```bash
    python generator.py generate
    ```
4. **Запустите пример запроса**:  
    ```bash
    python generator.py test
    ```  

## 💡 Команда генератора  

- [Алексей Малков](https://github.com/shft1)  
- [Владимир Кулаков](https://github.com/VladimirPulse)  
- [Даниил Колчак](https://github.com/Daniil-Kolchak)  
- [Данил Чирков](https://github.com/Dan1lChirkov)

---  

# 🔧 ***generator2***  

### 📚 Используемый стек и технологии:
- **Python 3.12+**
- **httpx (0.28.1)**: Для выполнения асинхронных HTTP-запросов.  
- **pydantic (2.10.4)**: Для определения моделей данных ввода и вывода.  
- **ruamel.yaml (0.18.6)**: Для работы с YAML файлами.  
- **openapi3-parser (1.1.19)**: Для парсинга OpenAPI спецификации.
- **ruff (0.7.1)**: Для автоматического исправления стилизации кода.
- **black (24.10.0)**: Для автоматического исправления стилизации кода.

## 📂 Структура генератора

### 🛠️ Основные компоненты

_src/generator2/generator2_full_

#### 📁 models/
- models_response_ # Модели ответов API
- models_reqBod_ # Модели запросов API

#### 🧩 bot.py
- Основной класс для работы с API
- Метакласс RequestMethodsCollector для сбора методов
- Базовая функциональность для HTTP-запросов
- Форматирование URL и параметров запросов

#### 🔧 constants.py
- Константы клиента
- Константы логгера

#### 🧪 pachca.py
- Пример использования сгенерированного API клиента
- Тестовые вызовы различных методов API

#### 📁 logger_setup.py
- Подготовка объекта логгера для логирования результатов работы

#### 🌐 request_methods.py
- Содержит асинхронные методы для работы с API
- Импортирует сгенерированные Pydantic модели
- Реализует логику HTTP-запросов

_src/generator2/services_

#### 🔧 constants.py
- Константы проекта
- Маппинги типов данных
- Пути к файлам
- HTTP методы

#### 💾 file_writer.py
- Обеспечивает безопасную запись файлов
- Создает необходимые директории
- Управляет генерацией выходных файлов

#### 📂 yaml_loader.py
- Загрузка YAML файла спецификации OpenAPI
- Создание глобального объекта YAML_DICT

#### 📁 logger_setup.py
- Подготовка объекта логгера для логирования результатов работы

_src/generator2/_

#### 📝 yaml_processor.py
- Обрабатывает YAML спецификацию
- Генерирует модели запросов и ответов
  - Функция get_all_endpoints для извлечения эндпоинтов из YAML документации
  - Функция process_endpoints для обработки эндпоинтов и генерации моделей для requestBody и response

#### 🔗 generate_pydantic_model.py
- Создает модели pydantic для конкретного эндпоинта
  - create_model для генерации текста модели pydantic
  -  create_enum для создания класса Enum
  - look_into_schema_new для рекурсивного прохода по модели спецификации и создания всех необходимых моделей
  - check_error_field для подмены тайпхинта в модели ошибок API

#### 🔗 schema_link_processor.py
- Обрабатывает ссылки на схемы в YAML спецификации
- Генерирует модели для ссылок на схемы
  - unite_schemas для объединения схем
  - load_schema для загрузки схемы по ссылке
  - new_replace_ref_with_schema для замены ссылок на схемы

#### 📜 requirements.txt
- Список зависимостей генератора с версиями

#### 🛠️ request_methods_generator.py
- Генерация методов для работы с API на основе OpenAPI спецификации
- Функции форматирования URL, параметров и обработки ответов

#### 📄 openapi.yaml:
- OpenAPI спецификации API
- Описание эндпоинтов, схем, параметров

#### 🛠️ generator_starter.py
- Основной запуск генерации необходимых файлов для клиента
- Форматтинг и правка сгенерированного кода в автоматическом режиме

---

## 🚀 Установка и использование

### 🛠️ Инструкция (работать в папке `src` при активированном `venv`):
1. **Создайте файл `.env`** в директории `generator2`, с токеном для работы с API "Пачка".  
Пример файла .env.example:  
    ```
    TOKEN=ваштокен
    ```
2. **Создайте и активируйте виртуальное окружение, установите зависимости**:  
    - Для Linux/gitBash:
        ```bash
        python3 -m venv venv  
        source venv/scripts/activate  
        pip install -r requirements.txt  
        ```  
    - Для Windows cmd: 
        ```bash
        python -m venv venv  
        .\venv\scripts\activate  
        pip install -r requirements.txt  
        ```  
3. **Запустите генерацию клиента**:  
    ```bash
    python -m generator2.generator_starter  
    ```  
4. **Запустите пример запроса**:  
    ```bash
    python -m generator2.generator2_full.pachca  
    ```  
    Или перейдите в `generator2` и запустите модуль:  
    ```bash
    cd generator2  
    python -m generator2_full.pachca  
    ```

## 💡 Команда генератора
- [Алексей Малков](https://github.com/shft1)  
- [Дмитрий Костин](https://github.com/k0sdm1)
- [Дмитрий Бурмистров](https://github.com/bura09906)
- [Павел Колесников](https://github.com/Mrclive7406)

---

# 🔧 ***builder***

## 🛠️ Инструменты для генерации библиотеки

### 📋 Порядок действий (работать в папке `builder` при активированном `venv`):

1. **Для запуска MakeFile командой make из VSCode нужно установить через PowerShell или cmd:**

    - winget install GnuWin32.Make.

2. **Создание зависимостей для работы сборки библиотеки:**

    ```bash
        pip install requirements_builder.txt  
    ```

3. **Создание зависимостей для библиотеки:**

    ```bash
        pipenv install requirements.txt  
    ```

4. **В папке проекта pachca_code_gen_team2 в файле .env указать:**
    - PACKAGE_VERSION=<Версия пакета>
    - TWINE_USERNAME=<Имя пользвателя сервиса TestPyPI>
    - TWINE_API_TOKEN=<Токен пользвателя сервиса TestPyPI>

4. **Запуск создания и загрузки библиотеки на серис TestPyPI при помощи команды:**

    ```bash
        make upload
    ```
5. **Установка бибилотеки с сериса TestPyPI:**

    - pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ PachcaAPI

5. **Запуск генератора и тестов:**

    - run_generate_and_test     - запуск генератора и тестов
    - run_generator             - запуск генератора
    - run_test                  - запуск тестов

## 📂 Структура генератора

_src/builder/_

#### 📜 requirements_builder.txt
- файл, содержащий список пакетов или библиотек, необходимых для работы упаковщика библиотеки.

#### 📜 requirements.txt
- файл, содержащий список пакетов или библиотек, необходимых для работы над библиотек.

#### 📄 Pipfile
- файл, используемый виртуальной средой Pipenv для управления зависимостями библиотек.

#### 🔒 Pipfile.lock
-  файл в формате JSON хранит контрольные суммы пакетов, которые устанавливаются в проект, что даёт гарантию, что развёрнутые на разных машинах окружения будут идентичны друг другу. 

#### 🛠️ Makefile 
- файл с инструкциями для утилиты make, которая нужна для автоматической сборки проекта.

#### 📦 setup.py
- файл с описанием, каким именно образом будет упакован код для медотов генерации

#### 📦 MANIFEST.in
- файл с указанием, какие файлы следует включить в сборку пакета 

---

## 💡 Команда упаковки генераторов

- [Алексей Малков](https://github.com/shft1)   
- [Александр Малыгин](https://github.com/SanyM2007)  
- [Александр Гора](https://github.com/MrAlexg82)

---

**📄 Документация API**: [Pachca API Documentation](https://crm.pachca.com/dev/getting-started/requests-and-responses/)

---
