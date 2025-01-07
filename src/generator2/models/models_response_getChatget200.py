from enum import Enum, IntEnum, StrEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Data(BaseModel):
    name: str = Field(..., description='Название')
    member_ids: Optional[List[int]] = Field(None, description='Массив идентификаторов пользователей, которые станут участниками')
    group_tag_ids: Optional[List[int]] = Field(None, description='Массив идентификаторов тегов, участников')
    channel: Optional[bool] = Field(None, description='Тип: беседа (по умолчанию, false) или канал (true)')
    public: Optional[bool] = Field(None, description='Доступ: закрытый (по умолчанию, false) или открытый (true)')
    id: Optional[int] = Field(None, description='Идентификатор беседы или канала')
    owner_id: Optional[int] = Field(None, description='Идентификатор пользователя, создавшего беседу или канал')
    created_at: Optional[str] = Field(None, description='Дата и время создания беседы или канала (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ')
    last_message_at: Optional[str] = Field(None, description='Дата и время создания последнего сообщения в беседе/канале (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ')
    meet_room_url: Optional[str] = Field(None, description='Ссылка на Видеочат')


class ResponseGetchatGet200(BaseModel):
    data: Optional[Data] = Field(None, description='No docstring provided')


