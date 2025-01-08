from enum import Enum, IntEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Buttons(BaseModel):
    text: Optional[str] = Field(None, description='No docstring provided')
    url: Optional[str] = Field(None, description='No docstring provided')
    data: Optional[str] = Field(None, description='No docstring provided')


class enum_file_type(str, Enum):
    file = 'file'
    image = 'image'


class Files(BaseModel):
    key: str = Field(..., description='Путь к файлу, полученный в результате загрузки файла (каждый файл в каждом сообщении должен иметь свой уникальный key, не допускается использование одного и того же key в разных сообщениях)')
    name: str = Field(..., description='Название файла, которое вы хотите отображать пользователю (рекомендуется писать вместе с расширением)')
    file_type: enum_file_type = Field(..., description='No docstring provided')
    id: Optional[int] = Field(None, description='No docstring provided')
    url: Optional[str] = Field(None, description='Прямая временная ссылка на скачивание файла')


class Thread(BaseModel):
    id: Optional[int] = Field(None, description='No docstring provided')
    chat_id: Optional[int] = Field(None, description='No docstring provided')


class Forwarding(BaseModel):
    original_message_id: Optional[int] = Field(None, description='Идентификатор оригинального сообщения')
    original_chat_id: Optional[int] = Field(None, description='Идентификатор чата, в котором находится оригинальное сообщение')
    author_id: Optional[int] = Field(None, description='Идентификатор чата, в котором находится оригинальное сообщение')
    original_created_at: Optional[int] = Field(None, description='Дата и время создания оригинального сообщения (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ')
    original_thread_id: Optional[int] = Field(None, description='Идентификатор треда, в котором находится оригинальное сообщение. Возвращается как null, если оригинальное сообщение не является комментарием в треде.')
    original_thread_message_id: Optional[int] = Field(None, description='Идентификатор сообщения, к которому был создан тред, в котором находится оригинальное сообщение. Возвращается как null, если оригинальное сообщение не является комментарием в треде.')
    original_thread_parent_chat_id: Optional[int] = Field(None, description='Идентификатор чата сообщения, к которому был создан тред, в котором находится оригинальное сообщение. Возвращается как null, если оригинальное сообщение не является комментарием в треде.')


class enum_entity_type(str, Enum):
    discussion = 'discussion'
    user = 'user'
    thread = 'thread'


class Data(BaseModel):
    content: str = Field(..., description='Текст сообщения')
    buttons: Optional[List[List[Buttons]]] = Field(None, description='No docstring provided')
    entity_type: Optional[enum_entity_type] = Field(None, description='No docstring provided')
    entity_id: int = Field(..., description='No docstring provided')
    parent_message_id: Optional[int] = Field(None, description='Идентификатор сообщения, к которому написан ответ. Возвращается как null, если сообщение не является ответом.')
    id: Optional[int] = Field(None, description='No docstring provided')
    chat_id: Optional[int] = Field(None, description='No docstring provided')
    user_id: Optional[int] = Field(None, description='No docstring provided')
    created_at: Optional[str] = Field(None, description='No docstring provided')
    files: Optional[List[Files]] = Field(None, description='No docstring provided')
    thread: Optional[Thread] = Field(None, description='No docstring provided')
    forwarding: Optional[Forwarding] = Field(None, description='No docstring provided')


class ResponseGetmessageGet200(BaseModel):
    data: Optional[Data] = Field(None, description='No docstring provided')


