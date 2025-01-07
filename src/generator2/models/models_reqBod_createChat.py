from enum import Enum, IntEnum, StrEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Chat(BaseModel):
    name: str = Field(..., description='Название')
    member_ids: Optional[List[int]] = Field(None, description='Массив идентификаторов пользователей, которые станут участниками')
    group_tag_ids: Optional[List[int]] = Field(None, description='Массив идентификаторов тегов, участников')
    channel: Optional[bool] = Field(None, description='Тип: беседа (по умолчанию, false) или канал (true)')
    public: Optional[bool] = Field(None, description='Доступ: закрытый (по умолчанию, false) или открытый (true)')


class Createchat(BaseModel):
    chat: Optional[Chat] = Field(None, description='Собранный объект параметров создаваемой беседы или канала')


