from enum import Enum, IntEnum
from typing import Any, Dict, Optional, List
from pydantic import Field, BaseModel


class Buttons(BaseModel):
    text: Optional[str] = Field(None, description="No docstring provided")
    url: Optional[str] = Field(None, description="No docstring provided")
    data: Optional[str] = Field(None, description="No docstring provided")


class enum_file_type(str, Enum):
    file = "file"
    image = "image"


class Files(BaseModel):
    key: str = Field(
        ...,
        description="Путь к файлу, полученный в результате загрузки файла (каждый файл в каждом сообщении должен иметь свой уникальный key, не допускается использование одного и того же key в разных сообщениях)",
    )
    name: str = Field(
        ...,
        description="Название файла, которое вы хотите отображать пользователю (рекомендуется писать вместе с расширением)",
    )
    file_type: enum_file_type = Field(..., description="No docstring provided")
    size: int = Field(
        ..., description="Размер файла в байтах, отображаемый пользователю"
    )


class Message(BaseModel):
    content: str = Field(..., description="Текст сообщения")
    buttons: Optional[List[List[Buttons]]] = Field(
        None, description="No docstring provided"
    )
    files: Optional[List[Files]] = Field(
        None, description="No docstring provided"
    )


class Editmessage(BaseModel):
    message: Optional[Message] = Field(
        None, description="No docstring provided"
    )
