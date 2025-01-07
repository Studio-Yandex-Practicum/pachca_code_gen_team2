import importlib
import inspect

import httpx
from constants import PARAM_NAME_SORT, PARAM_NAME_SORT_FIELD
from request_methods_generator import get_obj_openapi_spec


class RequestMethodsCollector(type):

    def __new__(cls, name, bases, dct):
        req_methods = importlib.import_module('request_methods')
        request_methods = cls.collect_methods(req_methods)

        for name_method, method in request_methods.items():
            dct[name_method] = method

        return super(
            RequestMethodsCollector, cls,
        ).__new__(cls, name, bases, dct)

    @staticmethod
    def collect_methods(module) -> dict[str, object]:
        """Собирает сгенерированные функции из модуля request_methods.py"""
        dict_func = {}

        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj):
                dict_func[name] = obj

        if not dict_func:
            raise ValueError(
                f"В модуле {module.__name__} "
                "отсутствуют сгенерированные функции",
            )

        return dict_func


class Bot(metaclass=RequestMethodsCollector):
    base_url = get_obj_openapi_spec().servers[0].url

    def __init__(self, token):
        self.token = token

    async def get_client(self):
        return httpx.AsyncClient(
            base_url=self.base_url,
            headers={'Authorization': self.token},
        )

    def format_url(
        self,
        url_template: str,
        path_param: dict[str, int] = None,
    ):
        return url_template.format(**path_param)

    def filter_query_params(self, **kwargs):
        if PARAM_NAME_SORT in kwargs or PARAM_NAME_SORT_FIELD in kwargs:
            sort = kwargs.pop(PARAM_NAME_SORT)
            sort_field = kwargs.pop(PARAM_NAME_SORT_FIELD)
            kwargs[f'sort[{sort_field}]'] = sort

        return {
            str(key): value
            for key, value in kwargs.items() if value is not None
        }
