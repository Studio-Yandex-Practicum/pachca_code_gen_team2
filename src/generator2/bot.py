import inspect
import httpx
import importlib

from request_methods_gen import get_obj_openapi_spec


TOKEN = 'Bearer '


class RequestMethodsCollector(type):

    def __new__(cls, name, bases, dct):
        req_methods = importlib.import_module('request_methods')
        request_methods = cls.collect_methods(req_methods)

        for name_method, method in request_methods.items():
            dct[name_method] = method

        return super(
            RequestMethodsCollector, cls
        ).__new__(cls, name, bases, dct)

    @staticmethod
    def collect_methods(module) -> dict[str, object]:
        """Собирает генерируемые функции из модуля request_methods.py"""
        dict_func = {}

        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj):
                dict_func[name] = obj

        if not dict_func:
            raise ValueError(
                f"В модуле {module.__name__} "
                "отсутствуют сгенерированные функции"
            )

        return dict_func


class PachcaBot(metaclass=RequestMethodsCollector):
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
        path_param: dict[str, int] = None
    ):
        return url_template.format(**path_param)
