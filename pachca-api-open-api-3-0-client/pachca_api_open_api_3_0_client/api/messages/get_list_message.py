from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.get_list_message_response_200 import GetListMessageResponse200
from ...models.not_found import NotFound
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chat_id: int,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chat_id"] = chat_id

    params["per"] = per

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, GetListMessageResponse200, NotFound]]:
    if response.status_code == 200:
        response_200 = GetListMessageResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if response.status_code == 400:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequest, GetListMessageResponse200, NotFound]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chat_id: int,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Response[Union[BadRequest, GetListMessageResponse200, NotFound]]:
    """получение списка сообщений чата

     Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.

    Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
    треда или диалога, и указать его в URL запроса. Сообщения будут возвращены
    в порядке убывания даты отправки (то есть, сначала будут идти последние сообщения чата).
    Для получения более ранних сообщений чата доступны параметры per и page.

    Args:
        chat_id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetListMessageResponse200, NotFound]]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        per=per,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    chat_id: int,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Optional[Union[BadRequest, GetListMessageResponse200, NotFound]]:
    """получение списка сообщений чата

     Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.

    Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
    треда или диалога, и указать его в URL запроса. Сообщения будут возвращены
    в порядке убывания даты отправки (то есть, сначала будут идти последние сообщения чата).
    Для получения более ранних сообщений чата доступны параметры per и page.

    Args:
        chat_id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetListMessageResponse200, NotFound]
    """

    return sync_detailed(
        client=client,
        chat_id=chat_id,
        per=per,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chat_id: int,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Response[Union[BadRequest, GetListMessageResponse200, NotFound]]:
    """получение списка сообщений чата

     Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.

    Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
    треда или диалога, и указать его в URL запроса. Сообщения будут возвращены
    в порядке убывания даты отправки (то есть, сначала будут идти последние сообщения чата).
    Для получения более ранних сообщений чата доступны параметры per и page.

    Args:
        chat_id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetListMessageResponse200, NotFound]]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        per=per,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getListMessage(
    *,
    client: Union[AuthenticatedClient, Client],
    chat_id: int,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Optional[Union[BadRequest, GetListMessageResponse200, NotFound]]:
    """получение списка сообщений чата

     Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.

    Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
    треда или диалога, и указать его в URL запроса. Сообщения будут возвращены
    в порядке убывания даты отправки (то есть, сначала будут идти последние сообщения чата).
    Для получения более ранних сообщений чата доступны параметры per и page.

    Args:
        chat_id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetListMessageResponse200, NotFound]
    """

    return (
        await asyncio_detailed(
            client=client,
            chat_id=chat_id,
            per=per,
            page=page,
        )
    ).parsed
