from typing import List, Optional

from pydantic import BaseModel, Field


class Data(BaseModel):
    user_id: Optional[int] = Field(
        None, description="Идентификатор пользователя, оставившего реакцию.",
    )
    created_at: Optional[str] = Field(
        None,
        description="Дата и время добавления реакции (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ.",
    )
    code: Optional[str] = Field(None, description="Emoji символ реакции.")


class ResponseGetmessagereactionsGet200(BaseModel):
    data: Optional[List[Data]] = Field(
        None, description="No docstring provided",
    )
