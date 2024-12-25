from http import HTTPStatus
from typing import Any, Optional

import httpx

from ... import errors
from ...types import Response


def _get_kwargs_delStatus(
    self,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/profile/status",
    }

    return _kwargs


def _parse_response_delStatus(self, response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_delStatus(self, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_delStatus(response=response),
    )


async def asyncio_detailed_delStatus(
    self,
) -> Response[Any]:
    """удаление своего статуса

     Параметры запроса отсутствуют

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = self._get_kwargs_delStatus()

    response = await self.client.get_async_httpx_client().request(**kwargs)

    return self._build_response_delStatus(response=response)
