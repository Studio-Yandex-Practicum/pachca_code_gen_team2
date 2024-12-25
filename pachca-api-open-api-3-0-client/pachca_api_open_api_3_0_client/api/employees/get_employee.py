from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.get_employee_response_200 import GetEmployeeResponse200
from ...models.not_found import NotFound
from ...types import Response


def _get_kwargs_getEmployee(
    self,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/{id}",
    }

    return _kwargs


def _parse_response_getEmployee(self, response: httpx.Response) -> Optional[Union[GetEmployeeResponse200, NotFound]]:
    if response.status_code == 200:
        response_200 = GetEmployeeResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getEmployee(self, response: httpx.Response) -> Response[Union[GetEmployeeResponse200, NotFound]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getEmployee(response=response),
    )


async def asyncio_detailed_getEmployee(
    self,
    id: int,
) -> Response[Union[GetEmployeeResponse200, NotFound]]:
    """получение информации о сотруднике

     Метод для получения информации о сотруднике.
    Для получения сотрудника вам необходимо знать его id и указать его в URL запроса.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetEmployeeResponse200, NotFound]]
    """

    kwargs = self._get_kwargs_getEmployee(
        id=id,
    )

    response = await self.client.get_async_httpx_client().request(**kwargs)

    return self._build_response_getEmployee(response=response)


async def getEmployee(
    self,
    id: int,
) -> Optional[Union[GetEmployeeResponse200, NotFound]]:
    """получение информации о сотруднике

     Метод для получения информации о сотруднике.
    Для получения сотрудника вам необходимо знать его id и указать его в URL запроса.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetEmployeeResponse200, NotFound]
    """

    return (
        await self.asyncio_detailed_getEmployee(
            id=id,
        )
    ).parsed
