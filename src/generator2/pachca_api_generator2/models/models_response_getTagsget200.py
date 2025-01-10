from enum import Enum, IntEnum, StrEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Data(BaseModel):
    id: Optional[int] = Field(None, description='Идентификатор тега')
    name: Optional[str] = Field(None, description='Название тега')
    users_count: Optional[int] = Field(None, description='Количество сотрудников, которые имеют этот тег')


class ResponseGettagsGet200(BaseModel):
    data: Optional[List[Data]] = Field(None, description='No docstring provided')


