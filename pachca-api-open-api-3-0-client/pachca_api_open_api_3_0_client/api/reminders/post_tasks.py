from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_tasks_body import PostTasksBody
from ...models.post_tasks_response_201 import PostTasksResponse201
from ...models.post_tasks_response_400 import PostTasksResponse400
from ...types import Response


def _get_kwargs(
    *,
    body: PostTasksBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tasks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostTasksResponse201, PostTasksResponse400]]:
    if response.status_code == 201:
        response_201 = PostTasksResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = PostTasksResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostTasksResponse201, PostTasksResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostTasksBody,
) -> Response[Union[PostTasksResponse201, PostTasksResponse400]]:
    """Метод для создания нового напоминания.

     При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
    простое напоминание, событие или письмо.
    При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
    текстом.
    Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
    У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

    Args:
        body (PostTasksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostTasksResponse201, PostTasksResponse400]]
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
    body: PostTasksBody,
) -> Optional[Union[PostTasksResponse201, PostTasksResponse400]]:
    """Метод для создания нового напоминания.

     При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
    простое напоминание, событие или письмо.
    При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
    текстом.
    Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
    У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

    Args:
        body (PostTasksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostTasksResponse201, PostTasksResponse400]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostTasksBody,
) -> Response[Union[PostTasksResponse201, PostTasksResponse400]]:
    """Метод для создания нового напоминания.

     При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
    простое напоминание, событие или письмо.
    При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
    текстом.
    Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
    У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

    Args:
        body (PostTasksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostTasksResponse201, PostTasksResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def post_tasks(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostTasksBody,
) -> Optional[Union[PostTasksResponse201, PostTasksResponse400]]:
    """Метод для создания нового напоминания.

     При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
    простое напоминание, событие или письмо.
    При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
    текстом.
    Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
    У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

    Args:
        body (PostTasksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostTasksResponse201, PostTasksResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
