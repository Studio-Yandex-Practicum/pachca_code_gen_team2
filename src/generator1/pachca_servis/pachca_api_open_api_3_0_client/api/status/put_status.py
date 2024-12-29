from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.bad_request import BadRequest
from ...models.put_status_response_201 import PutStatusResponse201
from ...models.query_status import QueryStatus
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_putStatus(
    self,
    body: QueryStatus,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/profile/status",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response_putStatus(self, response: httpx.Response) -> Optional[Union[BadRequest, PutStatusResponse201]]:
    if response.status_code == 201:
        response_201 = PutStatusResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_putStatus(self, response: httpx.Response) -> Response[Union[BadRequest, PutStatusResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_putStatus(response=response),
    )


async def putStatus(
    self,
    body: QueryStatus,
) -> Optional[Union[BadRequest, PutStatusResponse201]]:
    """новый статус

     Создание нового статуса.

    Args:
        body (QueryStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, PutStatusResponse201]
    """

    kwargs = self._get_kwargs_putStatus(
        body=body,
    )

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_putStatus(response=response).parsed
