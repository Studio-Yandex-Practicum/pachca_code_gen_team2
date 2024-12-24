from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_message_reactions_response_400 import DeleteMessageReactionsResponse400
from ...models.delete_message_reactions_response_404 import DeleteMessageReactionsResponse404
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    code: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/messages/{id}/reactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = DeleteMessageReactionsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = DeleteMessageReactionsResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
) -> Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
    """Удаление реакции

     Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены
    авторизованным пользователем.

    Args:
        id (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
) -> Optional[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
    """Удаление реакции

     Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены
    авторизованным пользователем.

    Args:
        id (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
        code=code,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
) -> Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
    """Удаление реакции

     Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены
    авторизованным пользователем.

    Args:
        id (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def deleteMessageReactions(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
) -> Optional[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
    """Удаление реакции

     Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены
    авторизованным пользователем.

    Args:
        id (str):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            code=code,
        )
    ).parsed
