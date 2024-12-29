import sys

PATH_TO_YAML = './src/generator2/openapi.yaml'

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
