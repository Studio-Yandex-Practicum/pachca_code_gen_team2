from enum import Enum, IntEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class enum_data_type(str, Enum):
    string = 'string'
    number = 'number'
    date = 'date'
    link = 'link'


class Custom_properties(BaseModel):
    id: Optional[int] = Field(None, description='Идентификатор поля')
    name: Optional[str] = Field(None, description='Название поля')
    data_type: Optional[enum_data_type] = Field(None, description='Тип поля (string, number, date или link)')
    value: Optional[str] = Field(None, description='Значение')


class enum_role(str, Enum):
    admin = 'admin'
    user = 'user'
    multi_guest = 'multi_guest'


class enum_invite_status(str, Enum):
    confirmed = 'confirmed'
    sent = 'sent'


class Data(BaseModel):
    id: Optional[int] = Field(None, description='Идентификатор пользователя')
    first_name: Optional[str] = Field(None, description='Имя')
    last_name: Optional[str] = Field(None, description='Фамилия')
    nickname: Optional[str] = Field(None, description='Имя пользователя')
    email: Optional[str] = Field(None, description='Электронная почта')
    phone_number: Optional[str] = Field(None, description='Телефон')
    department: Optional[str] = Field(None, description='Департамент')
    role: Optional[enum_role] = Field(None, description='Уровень доступа: admin (администратор), user (сотрудник), multi_guest (мульти-гость)')
    suspended: Optional[bool] = Field(None, description='Деактивация пользователя. При значении true пользователь является деактивированным.')
    invite_status: Optional[enum_invite_status] = Field(None, description='Статус приглашения: confirmed (принято), sent (отправлено)')
    list_tags: Optional[List[str]] = Field(None, description='Массив тегов, привязанных к сотруднику')
    custom_properties: Optional[List[Custom_properties]] = Field(None, description='Дополнительные поля сотрудника')
    bot: Optional[bool] = Field(None, description='Тип: пользователь (false) или бот (true)')


class ResponseGettagsemployeesGet200(BaseModel):
    data: Optional[List[Data]] = Field(None, description='No docstring provided')


