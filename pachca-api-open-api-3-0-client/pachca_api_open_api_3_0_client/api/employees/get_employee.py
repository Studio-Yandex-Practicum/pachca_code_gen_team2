from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_employee_response_200 import GetEmployeeResponse200
from ...models.not_found import NotFound
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetEmployeeResponse200, NotFound]]:
    if response.status_code == 200:
        response_200 = GetEmployeeResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetEmployeeResponse200, NotFound]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
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

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
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

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
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

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getEmployee(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
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
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
