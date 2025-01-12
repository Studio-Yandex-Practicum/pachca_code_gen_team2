from enum import StrEnum
from typing import List, Optional

from pydantic import BaseModel, Field


class Buttons(BaseModel):
    text: Optional[str] = Field(None, description="No docstring provided")
    url: Optional[str] = Field(None, description="No docstring provided")
    data: Optional[str] = Field(None, description="No docstring provided")


class enum_file_type(StrEnum):
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
        ..., description="Размер файла в байтах, отображаемый пользователю",
    )


class enum_entity_type(StrEnum):
    discussion = "discussion"
    user = "user"
    thread = "thread"


class Message(BaseModel):
    content: str = Field(..., description="Текст сообщения")
    buttons: Optional[List[List[Buttons]]] = Field(
        None, description="No docstring provided",
    )
    entity_type: Optional[enum_entity_type] = Field(
        None, description="No docstring provided",
    )
    entity_id: int = Field(..., description="No docstring provided")
    parent_message_id: Optional[int] = Field(
        None,
        description="Идентификатор сообщения, к которому написан ответ. Возвращается как null, если сообщение не является ответом.",
    )
    files: Optional[List[Files]] = Field(
        None, description="No docstring provided",
    )
    skip_invite_mentions: Optional[bool] = Field(
        None, description="No docstring provided",
    )
    link_preview: Optional[bool] = Field(
        None, description="No docstring provided",
    )


class Createmessage(BaseModel):
    message: Optional[Message] = Field(
        None, description="No docstring provided",
    )
