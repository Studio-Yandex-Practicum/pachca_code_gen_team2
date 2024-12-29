from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.create_task_body import CreateTaskBody
from ...models.create_task_response_201 import CreateTaskResponse201
from ...models.create_task_response_400 import CreateTaskResponse400
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_createTask(
    self,
    body: CreateTaskBody,
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


def _parse_response_createTask(
    self, response: httpx.Response
) -> Optional[Union[CreateTaskResponse201, CreateTaskResponse400]]:
    if response.status_code == 201:
        response_201 = CreateTaskResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateTaskResponse400.from_dict(response.json())

        return response_400
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_createTask(
    self, response: httpx.Response
) -> Response[Union[CreateTaskResponse201, CreateTaskResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_createTask(response=response),
    )


async def createTask(
    self,
    body: CreateTaskBody,
) -> Optional[Union[CreateTaskResponse201, CreateTaskResponse400]]:
    """Метод для создания нового напоминания.

     При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
    простое напоминание, событие или письмо.
    При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
    текстом.
    Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
    У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

    Args:
        body (CreateTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTaskResponse201, CreateTaskResponse400]
    """

    kwargs = self._get_kwargs_createTask(
        body=body,
    )

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_createTask(response=response).parsed
