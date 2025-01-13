from typing import List, Optional

from pydantic import BaseModel, Field


class Postmemberstochats(BaseModel):
    member_ids: List[int] = Field(
        ...,
        description="Массив идентификаторов пользователей, которые станут участниками",
    )
    silent: Optional[bool] = Field(
        None,
        description="Не создавать в чате системное сообщение о добавлении участника",
    )
