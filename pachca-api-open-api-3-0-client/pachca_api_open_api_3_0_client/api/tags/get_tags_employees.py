from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.get_tags_employees_response_200 import GetTagsEmployeesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["per"] = per

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/group_tags/{id}/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, GetTagsEmployeesResponse200]]:
    if response.status_code == 200:
        response_200 = GetTagsEmployeesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequest, GetTagsEmployeesResponse200]]:
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
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Response[Union[BadRequest, GetTagsEmployeesResponse200]]:
    """получение актуального списка сотрудников тега

     Метод для получения актуального списка сотрудников тега.

    Args:
        id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetTagsEmployeesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        per=per,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Optional[Union[BadRequest, GetTagsEmployeesResponse200]]:
    """получение актуального списка сотрудников тега

     Метод для получения актуального списка сотрудников тега.

    Args:
        id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetTagsEmployeesResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        per=per,
        page=page,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Response[Union[BadRequest, GetTagsEmployeesResponse200]]:
    """получение актуального списка сотрудников тега

     Метод для получения актуального списка сотрудников тега.

    Args:
        id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetTagsEmployeesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        per=per,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getTagsEmployees(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
) -> Optional[Union[BadRequest, GetTagsEmployeesResponse200]]:
    """получение актуального списка сотрудников тега

     Метод для получения актуального списка сотрудников тега.

    Args:
        id (int):
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetTagsEmployeesResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            per=per,
            page=page,
        )
    ).parsed
