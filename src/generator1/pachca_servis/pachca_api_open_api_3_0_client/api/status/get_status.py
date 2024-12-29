from http import HTTPStatus
from typing import Any, Optional

import httpx

from ... import errors
from ...models.get_status_response_200 import GetStatusResponse200
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_getStatus(
    self,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/profile/status",
    }

    return _kwargs


def _parse_response_getStatus(self, response: httpx.Response) -> Optional[GetStatusResponse200]:
    if response.status_code == 200:
        response_200 = GetStatusResponse200.from_dict(response.json())

        return response_200
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getStatus(self, response: httpx.Response) -> Response[GetStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getStatus(response=response),
    )


async def getStatus(
    self,
) -> Optional[GetStatusResponse200]:
    """получение информации о своем статусе

     Параметры запроса отсутствуют

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatusResponse200
    """

    kwargs = self._get_kwargs_getStatus()

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_getStatus(response=response).parsed
