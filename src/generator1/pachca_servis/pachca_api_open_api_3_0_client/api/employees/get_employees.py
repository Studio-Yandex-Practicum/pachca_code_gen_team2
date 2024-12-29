from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.get_employees_response_200 import GetEmployeesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs_getEmployees(
    self,
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
    query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["per"] = per

    params["page"] = page

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response_getEmployees(self, response: httpx.Response) -> Optional[GetEmployeesResponse200]:
    if response.status_code == 200:
        response_200 = GetEmployeesResponse200.from_dict(response.json())

        return response_200
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getEmployees(self, response: httpx.Response) -> Response[GetEmployeesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getEmployees(response=response),
    )


async def getEmployees(
    self,
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
    query: Union[Unset, str] = UNSET,
) -> Optional[GetEmployeesResponse200]:
    """получение актуального списка всех сотрудников компании

     Fetch a paginated list of employees with optional filtering by query.

    Args:
        per (Union[Unset, int]):  Default: 50.
        page (Union[Unset, int]):  Default: 1.
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEmployeesResponse200
    """

    kwargs = self._get_kwargs_getEmployees(
        per=per,
        page=page,
        query=query,
    )

    response = await self.client.get_async_httpx_client().request(**kwargs)

    return self._build_response_getEmployees(response=response).parsed
