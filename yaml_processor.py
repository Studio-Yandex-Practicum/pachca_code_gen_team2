from constants import HTTP_METHODS
from generate_pydantic_model import look_into_schema
from schema_link_processor import replace_ref_with_schema, load_schema
from yaml_loader import YAML_DICT


def get_all_endpoints(YAML_DICT: dict):
    endpoints = YAML_DICT.get('paths')
    method = {}
    for path, body in endpoints.items():
        for method_name in HTTP_METHODS:
            method_body = body.get(method_name)
            if method_body:
                method[method_name] = method_body
        for body in method.values():
            yield path, body
        method.clear()


def process_endpoints():
    body: dict
    for endpoint, body in get_all_endpoints(YAML_DICT):
        print(endpoint)
        operationId = body.get('operationId')

        print(operationId)
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
                            parameter.get('schema').get('type')
                        )
                    )
                else:
                    query_parameters.append(
                        (
                            parameter.get('name'),
                            parameter.get('schema').get('type')
                        )
                    )
        print('path: ', path_parameters)
        print('query: ', query_parameters)
        requestBody = body.get('requestBody')
        if requestBody:
            schema = (
                requestBody.get('content').get('application/json')
                or requestBody.get('content').get('multipart/form-data'))
            if not schema:
                break
            schema_has_link = schema.get('schema').get('$ref', False)
            schema = (
                {operationId.capitalize(): load_schema(schema_has_link)}
                if schema_has_link
                else {operationId.capitalize(): schema.get('schema')}
            )
            look_into_schema(replace_ref_with_schema(schema))
        print('='*80)


if __name__ == '__main__':
    process_endpoints()
