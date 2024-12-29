from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.get_tag_response_200 import GetTagResponse200
from ...models.get_tag_response_404 import GetTagResponse404
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_getTag(
    self,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/group_tags/{id}",
    }

    return _kwargs


def _parse_response_getTag(self, response: httpx.Response) -> Optional[Union[GetTagResponse200, GetTagResponse404]]:
    if response.status_code == 200:
        response_200 = GetTagResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetTagResponse404.from_dict(response.json())

        return response_404
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getTag(self, response: httpx.Response) -> Response[Union[GetTagResponse200, GetTagResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getTag(response=response),
    )


async def getTag(
    self,
    id: int,
) -> Optional[Union[GetTagResponse200, GetTagResponse404]]:
    """Информация о теге

     Параметры запроса отсутствуют

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagResponse200, GetTagResponse404]
    """

    kwargs = self._get_kwargs_getTag(
        id=id,
    )

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_getTag(response=response).parsed
