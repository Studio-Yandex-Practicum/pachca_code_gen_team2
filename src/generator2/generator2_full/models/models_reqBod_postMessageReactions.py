from pydantic import BaseModel, Field


class Postmessagereactions(BaseModel):
    code: str = Field(
        ..., description="Emoji в строковом формате для добавления реакции.",
    )
