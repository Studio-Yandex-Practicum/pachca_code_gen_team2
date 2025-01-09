from enum import Enum, IntEnum
from typing import Any, Dict, Optional, List
from pydantic import Field, BaseModel


class Posttagstochats(BaseModel):
    group_tag_ids: List[int] = Field(
        ...,
        description="Массив идентификаторов тегов, которые станут участниками",
    )
