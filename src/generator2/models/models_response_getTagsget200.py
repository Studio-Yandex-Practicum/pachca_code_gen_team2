from typing import List, Optional

from pydantic import BaseModel, Field


class Data(BaseModel):
    id: Optional[int] = Field(None, description="Идентификатор тега")
    name: Optional[str] = Field(None, description="Название тега")
    users_count: Optional[int] = Field(
        None, description="Количество сотрудников, которые имеют этот тег",
    )


class ResponseGettagsGet200(BaseModel):
    data: Optional[List[Data]] = Field(
        None, description="No docstring provided",
    )
