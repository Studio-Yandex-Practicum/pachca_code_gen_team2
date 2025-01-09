from typing import Optional

from pydantic import BaseModel, Field


class Data(BaseModel):
    id: Optional[int] = Field(None, description="Идентификатор тега")
    name: Optional[str] = Field(None, description="Название тега")
    users_count: Optional[int] = Field(
        None, description="Количество сотрудников, которые имеют этот тег",
    )


class ResponseGettagGet200(BaseModel):
    data: Optional[Data] = Field(
        None,
        description="Для получения тега вам необходимо знать его id и указать его в URL запроса.",
    )
