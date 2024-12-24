from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.create_message_body import CreateMessageBody
from ...models.create_message_response_201 import CreateMessageResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CreateMessageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, CreateMessageResponse201, list["Error"]]]:
    if response.status_code == 201:
        response_201 = CreateMessageResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for componentsschemas_errors_item_data in _response_404:
            componentsschemas_errors_item = Error.from_dict(componentsschemas_errors_item_data)

            response_404.append(componentsschemas_errors_item)

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
) -> Response[Union[BadRequest, CreateMessageResponse201, list["Error"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateMessageBody,
) -> Response[Union[BadRequest, CreateMessageResponse201, list["Error"]]]:
    r"""создание нового сообщения

     Метод для отправки сообщения в беседу или канал,
    личного сообщения пользователю или комментария в тред.

    При использовании entity_type: \"discussion\" (или просто без указания entity_type)
    допускается отправка любого chat_id в поле entity_id.
    То есть, сообщение можно отправить зная только идентификатор чата.
    При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
    или личное сообщение по идентификатору пользователя.

    Для отправки личного сообщения пользователю создавать чат не требуется.
    Достаточно указать entity_type: \"user\" и идентификатор пользователя.
    Чат будет создан автоматически, если между вами ещё не было переписки.
    Между двумя пользователями может быть только один личный чат.

    Args:
        body (CreateMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, CreateMessageResponse201, list['Error']]]
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
    body: CreateMessageBody,
) -> Optional[Union[BadRequest, CreateMessageResponse201, list["Error"]]]:
    r"""создание нового сообщения

     Метод для отправки сообщения в беседу или канал,
    личного сообщения пользователю или комментария в тред.

    При использовании entity_type: \"discussion\" (или просто без указания entity_type)
    допускается отправка любого chat_id в поле entity_id.
    То есть, сообщение можно отправить зная только идентификатор чата.
    При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
    или личное сообщение по идентификатору пользователя.

    Для отправки личного сообщения пользователю создавать чат не требуется.
    Достаточно указать entity_type: \"user\" и идентификатор пользователя.
    Чат будет создан автоматически, если между вами ещё не было переписки.
    Между двумя пользователями может быть только один личный чат.

    Args:
        body (CreateMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, CreateMessageResponse201, list['Error']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateMessageBody,
) -> Response[Union[BadRequest, CreateMessageResponse201, list["Error"]]]:
    r"""создание нового сообщения

     Метод для отправки сообщения в беседу или канал,
    личного сообщения пользователю или комментария в тред.

    При использовании entity_type: \"discussion\" (или просто без указания entity_type)
    допускается отправка любого chat_id в поле entity_id.
    То есть, сообщение можно отправить зная только идентификатор чата.
    При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
    или личное сообщение по идентификатору пользователя.

    Для отправки личного сообщения пользователю создавать чат не требуется.
    Достаточно указать entity_type: \"user\" и идентификатор пользователя.
    Чат будет создан автоматически, если между вами ещё не было переписки.
    Между двумя пользователями может быть только один личный чат.

    Args:
        body (CreateMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, CreateMessageResponse201, list['Error']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def createMessage(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateMessageBody,
) -> Optional[Union[BadRequest, CreateMessageResponse201, list["Error"]]]:
    r"""создание нового сообщения

     Метод для отправки сообщения в беседу или канал,
    личного сообщения пользователю или комментария в тред.

    При использовании entity_type: \"discussion\" (или просто без указания entity_type)
    допускается отправка любого chat_id в поле entity_id.
    То есть, сообщение можно отправить зная только идентификатор чата.
    При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
    или личное сообщение по идентификатору пользователя.

    Для отправки личного сообщения пользователю создавать чат не требуется.
    Достаточно указать entity_type: \"user\" и идентификатор пользователя.
    Чат будет создан автоматически, если между вами ещё не было переписки.
    Между двумя пользователями может быть только один личный чат.

    Args:
        body (CreateMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, CreateMessageResponse201, list['Error']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
