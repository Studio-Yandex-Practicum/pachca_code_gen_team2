from enum import Enum, IntEnum
from typing import Any, Dict, Optional, List
from pydantic import Field, BaseModel


class Data(BaseModel):
    id: Optional[int] = Field(None, description='No docstring provided')
    chat_id: Optional[int] = Field(None, description='No docstring provided')
    message_id: Optional[int] = Field(None, description='Идентификатор сообщения, к которому был создан тред.')
    message_chat_id: Optional[int] = Field(None, description='Идентификатор чата сообщения.')
    updated_at: Optional[str] = Field(None, description='Дата и время обновления треда (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ.')


class ResponseCreatethreadPost200(BaseModel):
    data: Optional[Data] = Field(None, description='No docstring provided')


