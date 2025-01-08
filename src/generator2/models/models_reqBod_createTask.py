from enum import Enum, IntEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Custom_properties(BaseModel):
    id: Optional[int] = Field(None, description='Идентификатор поля')
    value: Optional[str] = Field(None, description='Значение поля')


class enum_kind(str, Enum):
    call = 'call'
    meeting = 'meeting'
    reminder = 'reminder'
    event = 'event'
    email = 'email'


class enum_priority(IntEnum):
    priority_1 = 1
    priority_2 = 2
    priority_3 = 3


class Task(BaseModel):
    kind: enum_kind = Field(..., description='Тип напоминания')
    content: str = Field(..., description='Описание напоминания')
    due_at: str = Field(..., description='Срок выполнения напоминания (ISO-8601)')
    priority: Optional[enum_priority] = Field(None, description='Приоритет (1 - по умолчанию, 2 - важно, 3 - очень важно)')
    performer_ids: Optional[List[int]] = Field(None, description='Массив идентификаторов пользователей')
    custom_properties: Optional[List[Custom_properties]] = Field(None, description='No docstring provided')


class Createtask(BaseModel):
    task: Optional[Task] = Field(None, description='No docstring provided')


