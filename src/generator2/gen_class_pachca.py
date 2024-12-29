import inspect
import re
from typing import Union

import httpx
from openapi_parser import parse
from openapi_parser.specification import Path, Schema, Server, Specification

import api_methods

TOKEN = 'Bearer '


async def get_client(self):
    """Клиент генерируемого класса"""
    return httpx.AsyncClient(
        base_url=self.base_url,
        headers={'Authorization': TOKEN}
    )


def get_obj_openapi_spec(
        path_to_file='./src/generator2/openapi.yaml'
) -> Specification:
    """Читает спецификацию openapi из файла openapi.yaml и возвращает
    спецификацию в виде объекта Specification библиотеки openapi_parser"""
    with open(path_to_file, 'r', encoding='utf-8') as file:
        spec_openapi = file.read()

    return parse(spec_string=spec_openapi)


def collecting_class_properites(module) -> dict[str, Union[object, str]]:
    """Собирает генерируемые функции из модуля api_methods.py
    добавляет свойства класса и статичные функции."""
    dict_func = {}

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            dict_func[name] = obj

    dict_func['get_client'] = get_client

    return dict_func


def gen_template(paths: Path) -> list[str]:
    """Собирает параметры запроса всех paths спецификации
    Возвращает список шаблонов функций"""
    functions = []

    for path in paths:
        url = path.url
        for operation in path.operations:
            method_request = operation.method.value.lower()
            function_name = '_'.join(
                re.findall(r'[a-z]+|[A-Z][^A-Z]*', operation.operation_id)
            ).lower()
            docstring = (f'"""{operation.summary}\n'
                         f'\n{operation.description}"""')  # Создать функцию для редактирования docstring
            param_path = None
            param_query = {}
            # print(operation.parameters)
            for param in operation.parameters:
                if param.location.value == 'path':
                    param_path = param.name
                if param.location.value == 'query':
                    param_query[param.name] = param.schema.default if param.schema.default else None

        # print(url)
        functions.append(
            get_template_methods(
                function_name,
                url,
                method_request,
                param_path,
                param_query,
                docstring
            )
        )

    return functions


def get_template_methods(
        name_func,
        url,
        method_request,
        param_path,
        param_query,
        docstring
):
    """Возвращает шаблон генерируемой функции.
    Вызывается в функции gen_template"""
    if param_path:
        function_declaration = (f"async def {name_func}"
                                f"(self, {param_path}, param_query=None):")
        response = (f"response = await client.{method_request}"
                    f"(f'{url}', params=param_query)")
    else:
        function_declaration = f"async def {name_func}(self, param_query=None):"
        response = (f"response = await client.{method_request}"
                    f"('{url}', params=param_query)")
    return f"""
{function_declaration}
    {docstring}
    client = await self.get_client()
    async with client:
        {response}
        response.raise_for_status()
    return response.json()

"""


spec: Specification = get_obj_openapi_spec()
servers: list[Server] = spec.servers
paths: list[Path] = spec.paths
schemas: dict[str, Schema] = spec.schemas
base_url = base_url = servers[0].url

dict_properties_class = collecting_class_properites(api_methods)

dict_properties_class['get_client'] = get_client  # Добавляем метод get_client

dict_properties_class['base_url'] = base_url  # Добавляем свойство класса base_url

PachcaBot: object = type('PachcaBot', (object,), dict_properties_class)


if __name__ == "__main__":

    templates = gen_template(paths)

    with open(
        './src/generator2/api_methods.py', 'w', encoding='utf-8'
    ) as file:
        file.write('"""Сгенерированные методы запроса."""\n\n')
        for template in templates:
            file.write(template)
