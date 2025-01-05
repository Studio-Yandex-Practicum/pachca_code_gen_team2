import os
import re
import textwrap
from typing import Union

from httpx import codes
from openapi_parser import parse
from openapi_parser.specification import DataType, Path, Specification


def get_obj_openapi_spec(
        path_to_file='openapi.yaml',
) -> Specification:
    """Читает спецификацию openapi из файла openapi.yaml и возвращает
    спецификацию в виде объекта Specification библиотеки openapi_parser
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, path_to_file)

    with open(full_path, 'r', encoding='utf-8') as file:
        spec_openapi = file.read()

    return parse(spec_string=spec_openapi)


def get_template_methods(
        name_func: str,
        url: str,
        method_request: str,
        docstring: str,
        param_path: dict[str, Union[str, dict]] = None,
        param_query: dict[str, Union[str, dict]] = None,
        name_request_schema: str = None,
        name_response_schema: str = None,
        name_response_error_schema: str = None,
):
    """Возвращает шаблон генерируемой функции.
    Вызывается в функции gen_templates
    """
    function_params = []

    if param_path:
        for name, type_param in param_path.items():
            function_params.append(f'{name}: {type_param}')
    if param_query:
        for name, data_param in param_query.items():
            type_param = data_param['type']
            default_value = data_param['default']
            if name in {'sort', 'sort_field'}:
                default_value = f"'{default_value}'"
            function_params.append(f'{name}: {type_param} = {default_value}')

    if name_request_schema:
        function_params = ", ".join(["self", f"data: {name_request_schema}"] + function_params)
    else:
        function_params = ", ".join(["self"] + function_params)

    format_url = (
        f"url = self.format_url('{url}', {{"
        + ", ".join([f"'{name}': {name}" for name in param_path])
        + "})"
        if param_path else f"url = '{url}'"
    )

    filter_params = ""
    if param_query:
        query_params_for_filter = ", ".join([
            f"{name}={name}" for name in param_query.keys()
        ])
        filter_params = f'query_params=self.filter_query_params({query_params_for_filter})'

    if name_request_schema:
        get_response = f'response = await client.{method_request}(url, json=data.model_dump())'
    elif param_query:
        get_response = f'response = await client.{method_request}(url, params=query_params)'
    else:
        get_response = f"response = await client.{method_request}(url)"

    response_handling = ""
    if name_response_schema:
        response_handling += f"""
        if response.is_success:
            return {name_response_schema}.model_validate_json(response.text)"""
    if name_response_error_schema:
        response_handling += f"""
        if response.is_client_error:
            return {name_response_error_schema}.model_validate_json(response.text)"""

    response_annotation = f" -> {name_response_schema}" if name_response_schema else ""
    filter_params_code = f"\n        {filter_params}" if filter_params else ""

    return f"""

async def {name_func}({function_params}){response_annotation}:
    {docstring}
    client = await self.get_client()
    async with client:
        {format_url}{filter_params_code}
        {get_response}{response_handling}
"""


def format_docstring(summary: str, description: str, max_width: int = 79):
    """Редактирует длины строк докстринг
    генерируемых функций в соответствиие с PEP8
    """
    formatted_summary = "\n".join(textwrap.wrap(summary, width=max_width))
    formatted_description = "\n".join(
        textwrap.wrap(description, width=max_width),
    )
    return f'"""{formatted_summary}\n\n{formatted_description}"""'


def format_name_func(operation_id: str):
    """Возвращает название генерируемой функции запроса в требуемом формате"""
    return '_'.join(
        re.findall(r'[a-z]+|[A-Z][^A-Z]*', operation_id),
    ).lower()


def get_python_type(schema_type: DataType):
    """Сопоставляет текущий тип данных параметра с типом данных Python
    и возвращает его
    """
    type_mapping = {
        DataType.STRING: "str",
        DataType.INTEGER: "int",
        DataType.NUMBER: "float",
        DataType.BOOLEAN: "bool",
        DataType.ARRAY: "list",
        DataType.OBJECT: "dict",
    }

    return type_mapping.get(schema_type, None)


def gen_templates(paths: Path) -> list[str]:
    """Собирает параметры запроса всех paths спецификации
    передает их в функицю get_template_methods
    Возвращает список шаблонов функций
    """
    functions = []

    for path in paths:
        url = path.url
        for operation in path.operations:
            name_request_body_schema = None
            response_name_schema = None
            response_error_name_schema = None
            method_request = operation.method.value.lower()
            function_name = format_name_func(operation.operation_id)
            docstring = format_docstring(
                operation.summary, operation.description,
            )
            if operation.request_body:
                name_request_body_schema = operation.operation_id.capitalize()
            for response in operation.responses:
                if codes.is_success(response.code) and response.content:
                    response_name_schema = (
                        f'Response{operation.operation_id.capitalize()}'
                        f'{operation.method.value.capitalize()}'
                        f'{str(response.code).capitalize()}'
                    )
                if codes.is_client_error(response.code):
                    response_error_name_schema = (
                        f'Response{operation.operation_id.capitalize()}'
                        f'{operation.method.value.capitalize()}'
                        f'{str(response.code).capitalize()}'
                    )
            param_path = {}
            param_query = {}
            for param in operation.parameters:
                if param.location.value == 'path':
                    schema_type = get_python_type(param.schema.type)
                    param_path[param.name] = schema_type
                if param.location.value == 'query':
                    schema_type = get_python_type(param.schema.type)
                    if param.name == 'sort[id]':
                        default_value_sort = param.schema.default
                        param.name = 'sort'
                        param_query['sort_field'] = {
                            'type': 'str',
                            'default': 'id'
                        }
                        param_query[param.name] = {
                            'type': schema_type,
                            'default': default_value_sort
                        }
                        continue
                    param_query[param.name] = {
                        'type': schema_type,
                        'default': None,
                    }

            functions.append(
                get_template_methods(
                    function_name,
                    url,
                    method_request,
                    docstring,
                    param_path,
                    param_query,
                    name_request_body_schema,
                    response_name_schema,
                    response_error_name_schema
                ),
            )

    return functions


if __name__ == "__main__":

    spec: Specification = get_obj_openapi_spec()
    paths: list[Path] = spec.paths
    templates = gen_templates(paths)

    with open(
        'src/generator2/request_methods.py', 'w', encoding='utf-8',
    ) as file:
        file.write('"""Сгенерированные методы запроса."""\n\n')
        for template in templates:
            file.write(template)
