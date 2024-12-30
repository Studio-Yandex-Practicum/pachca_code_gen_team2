from constants import HTTP_METHODS
from generate_pydantic_model import look_into_schema_new
from schema_link_processor import load_schema
from yaml_loader import YAML_DICT


def get_all_endpoints(yaml_dict: dict):
    """Получает все эндпоинты из path документации."""
    endpoints = yaml_dict.get('paths')
    method = {}
    for path, body in endpoints.items():
        for method_name in HTTP_METHODS:
            method_body = body.get(method_name)
            if method_body:
                method[method_name] = method_body
        for body in method.values():
            yield path, body
        method.clear()


def process_endpoints() -> tuple[list, list]:
    """Обрабатывает эндпоинты."""
    body: dict
    for endpoint, body in get_all_endpoints(YAML_DICT):
        print(endpoint)
        operation_id = body.get('operationId')

        print(operation_id)
        parameters = body.get('parameters')
        path_parameters = []
        query_parameters = []
        if parameters:
            for parameter in parameters:
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
            schema = (
                request_body.get('content').get('application/json')
                or request_body.get('content').get('multipart/form-data'))
            if not schema:
                break
            schema_has_link = schema.get('schema').get('$ref', False)
            schema = (
                {operation_id.capitalize(): load_schema(schema_has_link)}
                if schema_has_link
                else {operation_id.capitalize(): schema.get('schema')}
            )
            look_into_schema_new(schema)

        print('='*80)
    return path_parameters, query_parameters


if __name__ == '__main__':
    process_endpoints()
