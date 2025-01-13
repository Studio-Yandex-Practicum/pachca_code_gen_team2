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

GENERATED_CLIENT_FOLDER = 'generator2_full'


TEMPLATE_CLASS_BOT = """
class Bot:
    base_url = URL
    token_type = TOKEN_TYPE

    def __init__(self, token):
        self.token = f'{self.token_type} {token}'

    async def get_client(self):
        return httpx.AsyncClient(
            base_url=self.base_url,
            headers={'Authorization': self.token},
        )

    async def format_url(
        self,
        url_template: str,
        path_param: dict[str, int] = None,
    ):
        return url_template.format(**path_param)

    async def filter_query_params(self, **kwargs):
        if PARAM_NAME_SORT in kwargs or PARAM_NAME_SORT_FIELD in kwargs:
            sort = kwargs.pop(PARAM_NAME_SORT)
            sort_field = kwargs.pop(PARAM_NAME_SORT_FIELD)
            kwargs[f'sort[{sort_field}]'] = sort

        return {
            str(key): value
            for key, value in kwargs.items() if value is not None
        }

"""

TEMPLATE_IMPORT_FOR_CLASS_BOT = """
import httpx

from .constants import PARAM_NAME_SORT, PARAM_NAME_SORT_FIELD, TOKEN_TYPE, URL
"""
