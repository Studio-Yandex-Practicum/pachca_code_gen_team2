import re
import os
import textwrap

from openapi_parser import parse
from openapi_parser.specification import Path, Specification, DataType


def get_obj_openapi_spec(
        path_to_file='openapi.yaml'
) -> Specification:
    """Читает спецификацию openapi из файла openapi.yaml и возвращает
    спецификацию в виде объекта Specification библиотеки openapi_parser"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, path_to_file)

    with open(full_path, 'r', encoding='utf-8') as file:
        spec_openapi = file.read()

    return parse(spec_string=spec_openapi)


def get_template_methods(
        name_func,
        url,
        method_request,
        param_path: dict,
        param_query: dict,
        docstring
):
    """Возвращает шаблон генерируемой функции.
    Вызывается в функции gen_template"""
    function_params = []
    if param_path:
        for name, type_param in param_path.items():
            function_params.append(f'{name}: {type_param}')
    if param_query:
        for name, type_param in param_query.items():
            function_params.append(f'{name}: {type_param} = None')
    function_params = ", ".join(["self"] + function_params)

    format_url = (
        f"url = self.format_url('{url}', {{"
        + ", ".join([f"'{name}': {name}" for name in param_path])
        + "})"
        if param_path else f"url = '{url}'"
    )

    get_response = (
        f"response = await client.{method_request}(url"
        + (f", params={param_query}" if param_query else "")
        + ")"
    )

    if param_query:
        query_params = ", ".join([
            f"'{name}': {name}" for name in param_query.keys()
        ])
        get_response = f"response = await client.{method_request}(url, params={{ {query_params} }})"
    else:
        get_response = f"response = await client.{method_request}(url)"

    return f"""

async def {name_func}({function_params}):
    {docstring}
    client = await self.get_client()
    async with client:
        {format_url}
        {get_response}
        response.raise_for_status()
    return response.json()
"""


def format_docstring(summary: str, description: str, max_width: int = 79):
    """Редактирует длины строк докстринг
    генерируемых функций в соответствиие с PEP8"""
    formatted_summary = "\n".join(textwrap.wrap(summary, width=max_width))
    formatted_description = "\n".join(
        textwrap.wrap(description, width=max_width)
    )
    return f'"""{formatted_summary}\n\n{formatted_description}"""'


def format_name_func(operation_id: str):
    "Возвращает название генерируемой функции запроса в требуемом формате"
    return '_'.join(
        re.findall(r'[a-z]+|[A-Z][^A-Z]*', operation_id)
    ).lower()


def get_python_type(schema_type: DataType):
    """Сопоставляет текущий тип данных параметра с типом данных Python
    и возвращает его"""
    type_mapping = {
        DataType.STRING: "str",
        DataType.INTEGER: "int",
        DataType.NUMBER: "float",
        DataType.BOOLEAN: "bool",
        DataType.ARRAY: "list",
        DataType.OBJECT: "dict",
    }

    return type_mapping.get(schema_type, None)


def gen_template(paths: Path) -> list[str]:
    """Собирает параметры запроса всех paths спецификации
    Возвращает список шаблонов функций"""
    functions = []

    for path in paths:
        url = path.url
        for operation in path.operations:
            method_request = operation.method.value.lower()
            function_name = format_name_func(operation.operation_id)
            docstring = format_docstring(
                operation.summary, operation.description
            )
            param_path = {}
            param_query = {}
            #for obj in operation.request_body.content:
            #    print(obj.schema.title)
            #print(operation.request_body.content)
            for param in operation.parameters:
                if param.location.value == 'path':
                    schema_type = get_python_type(param.schema.type)
                    print(schema_type)
                    param_path[param.name] = schema_type
                if param.location.value == 'query':
                    schema_type = get_python_type(param.schema.type)
                    param_query[param.name] = schema_type

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


if __name__ == "__main__":

    spec: Specification = get_obj_openapi_spec()
    paths: list[Path] = spec.paths

    templates = gen_template(paths)

    with open(
        'src/generator2/request_methods.py', 'w', encoding='utf-8'
    ) as file:
        file.write('"""Сгенерированные методы запроса."""\n\n')
        for template in templates:
            file.write(template)
