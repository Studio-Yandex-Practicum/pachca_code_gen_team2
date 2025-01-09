from enum import Enum, IntEnum
from typing import Any, Dict, Optional, List
from pydantic import Field, BaseModel


class Postmemberstochats(BaseModel):
    member_ids: List[int] = Field(..., description='Массив идентификаторов пользователей, которые станут участниками')
    silent: Optional[bool] = Field(None, description='Не создавать в чате системное сообщение о добавлении участника')


