from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_chat_body import CreateChatBody
from ...models.create_chat_response_201 import CreateChatResponse201
from ...models.create_chat_response_400 import CreateChatResponse400
from ...models.create_chat_response_404 import CreateChatResponse404
from ...models.create_chat_response_422 import CreateChatResponse422
from ...types import Response


def _get_kwargs(
    *,
    body: CreateChatBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chats",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
    if response.status_code == 201:
        response_201 = CreateChatResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateChatResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = CreateChatResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = CreateChatResponse422.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChatBody,
) -> Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
    r""" Новая беседа или канал

     Метод для создания новой беседы или нового канала.
    При создании беседы или канала вы автоматически становитесь участником.\

    Args:
        body (CreateChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]
     """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChatBody,
) -> Optional[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
    r""" Новая беседа или канал

     Метод для создания новой беседы или нового канала.
    При создании беседы или канала вы автоматически становитесь участником.\

    Args:
        body (CreateChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]
     """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChatBody,
) -> Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
    r""" Новая беседа или канал

     Метод для создания новой беседы или нового канала.
    При создании беседы или канала вы автоматически становитесь участником.\

    Args:
        body (CreateChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]
     """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def createChat(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateChatBody,
) -> Optional[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
    r""" Новая беседа или канал

     Метод для создания новой беседы или нового канала.
    При создании беседы или канала вы автоматически становитесь участником.\

    Args:
        body (CreateChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
