from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.get_chat_response_200 import GetChatResponse200
from ...models.get_chat_response_404 import GetChatResponse404
from ...types import Response


def _get_kwargs_getChat(
    self,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/chats/{id}",
    }

    return _kwargs


def _parse_response_getChat(self, response: httpx.Response) -> Optional[Union[GetChatResponse200, GetChatResponse404]]:
    if response.status_code == 200:
        response_200 = GetChatResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetChatResponse404.from_dict(response.json())

        return response_404
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getChat(self, response: httpx.Response) -> Response[Union[GetChatResponse200, GetChatResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getChat(response=response),
    )


async def asyncio_detailed_getChat(
    self,
    id: int,
) -> Response[Union[GetChatResponse200, GetChatResponse404]]:
    """Информация о беседе или канале

     Получения информации о беседе или канале.
    Для получения беседы или канала вам необходимо знать её id и указать его в URL запроса.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChatResponse200, GetChatResponse404]]
    """

    kwargs = self._get_kwargs_getChat(
        id=id,
    )

    response = await self.client.get_async_httpx_client().request(**kwargs)

    return self._build_response_getChat(response=response)


async def getChat(
    self,
    id: int,
) -> Optional[Union[GetChatResponse200, GetChatResponse404]]:
    """Информация о беседе или канале

     Получения информации о беседе или канале.
    Для получения беседы или канала вам необходимо знать её id и указать его в URL запроса.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChatResponse200, GetChatResponse404]
    """

    return (
        await self.asyncio_detailed_getChat(
            id=id,
        )
    ).parsed
