from enum import StrEnum
from typing import List, Optional

from pydantic import BaseModel, Field


class enum_data_type(StrEnum):
    string = "string"
    number = "number"
    date = "date"
    link = "link"


class Data(BaseModel):
    id: Optional[int] = Field(None, description="Название поля")
    name: Optional[str] = Field(None, description="Идентификатор поля")
    data_type: Optional[enum_data_type] = Field(None, description="тип поля")


class ResponseGetcommonmethodsGet200(BaseModel):
    data: Optional[List[Data]] = Field(
        None, description="No docstring provided",
    )
