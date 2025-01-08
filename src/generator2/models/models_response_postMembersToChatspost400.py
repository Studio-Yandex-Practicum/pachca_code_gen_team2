from enum import Enum, IntEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Errors(BaseModel):
    key: Optional[str] = Field(None, description='Ключ параметра, в котором произошла ошибка')
    value: Optional[str] = Field(None, description='Значение ключа, которое вызвало ошибку')
    message: Optional[str] = Field(None, description='Ошибка текстом, который вы можете вывести пользователю')
    code: Optional[str] = Field(None, description='Внутренний код ошибки (коды ошибок представлены в описании каждого метода)')
    payload: Optional[Dict] = Field(None, description='Объект, который предоставляет любую дополнительную информацию (возможные дополнения представлены в описании каждого метода)')


class ResponsePostmemberstochatsPost400(BaseModel):
    errors: Optional[List[Errors]] = Field(None, description='No docstring provided')


