from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_message_reactions_body import PostMessageReactionsBody
from ...models.post_message_reactions_response_400 import PostMessageReactionsResponse400
from ...models.post_message_reactions_response_403 import PostMessageReactionsResponse403
from ...models.post_message_reactions_response_404 import PostMessageReactionsResponse404
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PostMessageReactionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/messages/{id}/reactions",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PostMessageReactionsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = PostMessageReactionsResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = PostMessageReactionsResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
]:
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
    body: PostMessageReactionsBody,
) -> Response[
    Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
]:
    """Добавление реакции

     Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый пользователь может
    установить не более 20 уникальных реакций на сообщение. - Сообщение может иметь не более 30
    уникальных реакций. - Сообщение может иметь не более 1000 реакций.

    Args:
        id (str):
        body (PostMessageReactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageReactionsBody,
) -> Optional[
    Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
]:
    """Добавление реакции

     Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый пользователь может
    установить не более 20 уникальных реакций на сообщение. - Сообщение может иметь не более 30
    уникальных реакций. - Сообщение может иметь не более 1000 реакций.

    Args:
        id (str):
        body (PostMessageReactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageReactionsBody,
) -> Response[
    Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
]:
    """Добавление реакции

     Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый пользователь может
    установить не более 20 уникальных реакций на сообщение. - Сообщение может иметь не более 30
    уникальных реакций. - Сообщение может иметь не более 1000 реакций.

    Args:
        id (str):
        body (PostMessageReactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def postMessageReactions(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageReactionsBody,
) -> Optional[
    Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
]:
    """Добавление реакции

     Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый пользователь может
    установить не более 20 уникальных реакций на сообщение. - Сообщение может иметь не более 30
    уникальных реакций. - Сообщение может иметь не более 1000 реакций.

    Args:
        id (str):
        body (PostMessageReactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
