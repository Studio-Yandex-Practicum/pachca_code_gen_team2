from enum import Enum, IntEnum, StrEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Posttagstochats(BaseModel):
    group_tag_ids: List[int] = Field(..., description='Массив идентификаторов тегов, которые станут участниками')


