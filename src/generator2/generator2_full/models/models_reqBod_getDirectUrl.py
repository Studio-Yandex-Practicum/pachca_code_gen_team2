from typing import Optional

from pydantic import BaseModel, Field


class Getdirecturl(BaseModel):
    Content_Disposition: Optional[str] = Field(
        None,
        description="Используемый заголовок",
        alilas="Content-Disposition",
    )
    acl: Optional[str] = Field(None, description="Уровень безопасности")
    policy: Optional[str] = Field(
        None, description="Уникальный policy для загрузки файла",
    )
    x_amz_credential: Optional[str] = Field(
        None,
        description="x-amz-credential для загрузки файла",
        alilas="x-amz-credential",
    )
    x_amz_algorithm: Optional[str] = Field(
        None, description="Используемый алгоритм", alilas="x-amz-algorithm",
    )
    x_amz_date: Optional[str] = Field(
        None,
        description="Уникальный x-amz-date для загрузки файла",
        alilas="x-amz-date",
    )
    x_amz_signature: Optional[str] = Field(
        None,
        description="Уникальная подпись для загрузки файла",
        alilas="x-amz-signature",
    )
    key: Optional[str] = Field(
        None, description="Уникальный ключ для загрузки файла",
    )
    file: Optional[str] = Field(None, description="Адрес для загрузки файла")
