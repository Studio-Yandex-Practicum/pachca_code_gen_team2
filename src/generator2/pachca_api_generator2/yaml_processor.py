import sys
from .constants import HTTP_METHODS
from .file_writer import write_to_file
from .generate_pydantic_model import look_into_schema_new
from .schema_link_processor import load_schema
from .yaml_loader import YAML_DICT


def get_all_endpoints(yaml_dict: dict):
    """Получает все эндпоинты из path документации."""
    endpoints = yaml_dict.get('paths')
    method = {}
    for path, body in endpoints.items():
        for method_name in HTTP_METHODS:
            method_body = body.get(method_name)
            if method_body:
                method[method_name] = method_body
        for name, body in method.items():
            yield path, name, body
        method.clear()


def process_endpoints() -> tuple[list, list]:
    """Обрабатывает эндпоинты.

    Проходит по каждому эндпоинту в openapi файле и генерирует модели для
    каждой схемы в requestBody и resopnse.
    """
    
    body: dict
    for endpoint, method, body in get_all_endpoints(YAML_DICT):
        print(endpoint, method)
        operation_id = body.get('operationId')
        print(operation_id)
        parameters = body.get('parameters')
        path_parameters = []
        query_parameters = []
        if parameters:
            for parameter in parameters:
                if '$ref' in parameter:
                    parameter = load_schema(parameter['$ref'], is_parameter=1)
                required = parameter.get('required', False)
                if required:
                    path_parameters.append(
                        (
                            parameter.get('name'),
                            parameter.get('schema').get('type'),
                        ),
                    )
                else:
                    query_parameters.append(
                        (
                            parameter.get('name'),
                            parameter.get('schema').get('type'),
                        ),
                    )
        print('path: ', path_parameters)
        print('query: ', query_parameters)
        request_body = body.get('requestBody')
        if request_body:
            write_to_file(
                f'models_reqBod_{operation_id}',
                (
                    'from enum import Enum, IntEnum'
                    f'{"" if sys.version_info[1] < 11 else ", StrEnum"}\n'
                    'from typing import Dict, Optional, List\n'
                    'from pydantic import Field, BaseModel\n\n\n'
                ),
                'w'
            )
            schema = (
                request_body.get('content').get('application/json')
                or request_body.get('content').get('multipart/form-data'))
            if not schema:
                continue
            schema_has_link = schema.get('schema').get('$ref', False)
            schema = (
                {operation_id.capitalize(): load_schema(schema_has_link)}
                if schema_has_link
                else {operation_id.capitalize(): schema.get('schema')}
            )
            look_into_schema_new(schema, 'models_reqBod_' + operation_id)
        # print('\nRequestBodyEnd+++++++++++++++++++++++++++++++++++++++++++++\nResponses start\n')
        try:
            responses = body.get('responses', False)
            if responses:
                for code, response in responses.items():
                    if 'content' not in response:
                        continue
                    schema = (
                        response.get('content').get('application/json')
                        or response.get('content').get('multipart/form-data'))
                    if not schema:
                        continue
                    write_to_file(
                        f'models_response_{operation_id}{method}{code}',
                        (
                            'from enum import Enum, IntEnum'
                            f'{"" if sys.version_info[1] < 11 else ", StrEnum"}\n'
                            'from typing import Dict, Optional, List\n'
                            'from pydantic import Field, BaseModel\n\n\n'
                        ),
                        'w'
                    )
                    schema_has_link = schema.get('schema').get('$ref', False)
                    model_name = (
                        f'Response{operation_id.capitalize()}'
                        f'{method.capitalize()}{code}')
                    schema = (
                        {model_name: load_schema(schema_has_link)}
                        if schema_has_link
                        else {model_name: schema.get('schema')}
                    )
                    look_into_schema_new(
                        schema,
                        f'models_response_{operation_id}{method}{code}'
                    )
        except Exception as e:
            print(f'Unable to create responses for {operation_id, method, code}!!!')
            print(e)
        print('='*80)
    return path_parameters, query_parameters


if __name__ == '__main__':
    process_endpoints()
