from typing import List

from pydantic import BaseModel, Field


class Posttagstochats(BaseModel):
    group_tag_ids: List[int] = Field(
        ...,
        description="Массив идентификаторов тегов, которые станут участниками",
    )
