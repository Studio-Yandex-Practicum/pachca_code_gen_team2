from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_employees_response_200 import GetEmployeesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetEmployeesResponse200]:
    if response.status_code == 200:
        response_200 = GetEmployeesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetEmployeesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
    query: Union[Unset, str] = UNSET,
) -> Response[GetEmployeesResponse200]:
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
        Response[GetEmployeesResponse200]
    """

    kwargs = _get_kwargs(
        per=per,
        page=page,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
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

    return sync_detailed(
        client=client,
        per=per,
        page=page,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
    query: Union[Unset, str] = UNSET,
) -> Response[GetEmployeesResponse200]:
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
        Response[GetEmployeesResponse200]
    """

    kwargs = _get_kwargs(
        per=per,
        page=page,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getEmployees(
    *,
    client: Union[AuthenticatedClient, Client],
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

    return (
        await asyncio_detailed(
            client=client,
            per=per,
            page=page,
            query=query,
        )
    ).parsed
