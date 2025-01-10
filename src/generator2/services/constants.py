from pathlib import Path
import sys

# PATH_TO_YAML = './openapi_test.yaml'
PATH_TO_YAML = (
    f'{Path(__file__).parent.parent.resolve()}/openapi.yaml')
SPECIFICATION_FILE_NAME = (
    f'{Path(__file__).parent.parent.resolve()}/openapi.yaml')

PYTHON_TYPES = {
    'string': 'str',
    'integer': 'int',
    'boolean': 'bool',
}

ENUM_TYPES = {
    'string': 'str, Enum' if sys.version_info[1] < 11 else 'StrEnum',
    'integer': 'IntEnum',
}

HTTP_METHODS = (
    'get', 'post', 'put', 'update', 'patch', 'delete',
)

PARAM_TYPE_KEY = 'type'
PARAM_DEFAULT_KEY = 'default'

SCHEMA_SORT_ID = 'sort[id]'
PARAM_NAME_SORT = 'sort'
PARAM_NAME_SORT_FIELD = 'sort_field'

PARAM_LOCATION_QUERY = 'query'
PARAM_LOCATION_PATH = 'path'

PREFIX_RESPONSE = 'models_response_'
PREFIX_REQUEST = 'models_reqBod_'

DEFAULT_VALUE_SORT_FIELD = 'id'
TYPE_SORT_FIELD = 'str'

LOG_FILE_NAME = 'client_generator.log'
