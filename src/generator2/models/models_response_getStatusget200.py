from enum import Enum, IntEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Data(BaseModel):
    emoji: Optional[str] = Field(None, description='Emoji символ статуса')
    title: Optional[str] = Field(None, description='Текст статуса')
    expires_at: Optional[str] = Field(None, description='Срок жизни статуса (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ. Возвращается как null, если срок не установлен.')


class ResponseGetstatusGet200(BaseModel):
    data: Optional[Data] = Field(None, description='Статус. Возвращается как null, если статус не установлен.')


