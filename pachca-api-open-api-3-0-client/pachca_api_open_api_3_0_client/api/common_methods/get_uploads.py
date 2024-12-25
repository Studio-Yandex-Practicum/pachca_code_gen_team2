from http import HTTPStatus
from typing import Any, Optional

import httpx

from ... import errors
from ...models.file_response import FileResponse
from ...types import Response


def _get_kwargs_getUploads(
    self,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/uploads",
    }

    return _kwargs


def _parse_response_getUploads(self, response: httpx.Response) -> Optional[FileResponse]:
    if response.status_code == 200:
        response_200 = FileResponse.from_dict(response.json())

        return response_200
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getUploads(self, response: httpx.Response) -> Response[FileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getUploads(response=response),
    )


async def asyncio_detailed_getUploads(
    self,
) -> Response[FileResponse]:
    """Получение подписи и ключа для загрузки файла

     Возвращает параметры, необходимые для безопасной загрузки файла.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileResponse]
    """

    kwargs = self._get_kwargs_getUploads()

    response = await self.client.get_async_httpx_client().request(**kwargs)

    return self._build_response_getUploads(response=response)


async def getUploads(
    self,
) -> Optional[FileResponse]:
    """Получение подписи и ключа для загрузки файла

     Возвращает параметры, необходимые для безопасной загрузки файла.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileResponse
    """

    return (await self.asyncio_detailed_getUploads()).parsed
