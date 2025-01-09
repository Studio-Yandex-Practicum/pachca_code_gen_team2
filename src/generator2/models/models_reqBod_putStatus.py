from enum import Enum, IntEnum
from typing import Any, Dict, Optional, List
from pydantic import Field, BaseModel


class Status(BaseModel):
    emoji: Optional[str] = Field(None, description="Emoji символ статуса")
    title: Optional[str] = Field(None, description="Текст статуса")
    expires_at: Optional[str] = Field(
        None,
        description="Срок жизни статуса (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ. Возвращается как null, если срок не установлен.",
    )


class Putstatus(BaseModel):
    status: Optional[Status] = Field(
        None,
        description="Статус. Возвращается как null, если статус не установлен.",
    )
