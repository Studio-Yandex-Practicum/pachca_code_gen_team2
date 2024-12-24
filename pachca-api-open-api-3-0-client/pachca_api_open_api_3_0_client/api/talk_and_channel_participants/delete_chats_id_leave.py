from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_code import ErrorsCode
from ...types import Response


def _get_kwargs_delete_chats_id_leave(
    self,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/chats/{id}/leave",
    }

    return _kwargs


def _parse_response_delete_chats_id_leave(
    self, *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ErrorsCode"]]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ErrorsCode.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400
    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ErrorsCode.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_delete_chats_id_leave(
    self, *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["ErrorsCode"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_delete_chats_id_leave(client=client, response=response),
    )


async def asyncio_detailed_delete_chats_id_leave(
    self,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list["ErrorsCode"]]]:
    """Выход из беседы или канала

     Метод для самостоятельного выхода из беседы или канала.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ErrorsCode']]]
    """

    kwargs = self._get_kwargs_delete_chats_id_leave(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return self._build_response_delete_chats_id_leave(client=client, response=response)


async def delete_chats_id_leave(
    self,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list["ErrorsCode"]]]:
    """Выход из беседы или канала

     Метод для самостоятельного выхода из беседы или канала.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ErrorsCode']]
    """

    return (
        await self.asyncio_detailed_delete_chats_id_leave(
            id=id,
            client=client,
        )
    ).parsed
