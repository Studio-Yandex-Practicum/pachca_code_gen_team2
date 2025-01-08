from enum import Enum, IntEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Postmessagereactions(BaseModel):
    code: str = Field(..., description='Emoji в строковом формате для добавления реакции.')


