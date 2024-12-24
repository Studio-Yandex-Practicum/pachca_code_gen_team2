from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_response_200 import GetTagsResponse200
from ...models.get_tags_response_400 import GetTagsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["per"] = per

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group_tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetTagsResponse200, GetTagsResponse400]]:
    if response.status_code == 200:
        response_200 = GetTagsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetTagsResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetTagsResponse200, GetTagsResponse400]]:
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
) -> Response[Union[GetTagsResponse200, GetTagsResponse400]]:
    """Список тегов сотрудников

     Метод для получения актуального списка тегов сотрудников.

    Args:
        per (Union[Unset, int]):  Default: 50.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTagsResponse200, GetTagsResponse400]]
    """

    kwargs = _get_kwargs(
        per=per,
        page=page,
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
) -> Optional[Union[GetTagsResponse200, GetTagsResponse400]]:
    """Список тегов сотрудников

     Метод для получения актуального списка тегов сотрудников.

    Args:
        per (Union[Unset, int]):  Default: 50.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagsResponse200, GetTagsResponse400]
    """

    return sync_detailed(
        client=client,
        per=per,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
) -> Response[Union[GetTagsResponse200, GetTagsResponse400]]:
    """Список тегов сотрудников

     Метод для получения актуального списка тегов сотрудников.

    Args:
        per (Union[Unset, int]):  Default: 50.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTagsResponse200, GetTagsResponse400]]
    """

    kwargs = _get_kwargs(
        per=per,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getTags(
    *,
    client: Union[AuthenticatedClient, Client],
    per: Union[Unset, int] = 50,
    page: Union[Unset, int] = 1,
) -> Optional[Union[GetTagsResponse200, GetTagsResponse400]]:
    """Список тегов сотрудников

     Метод для получения актуального списка тегов сотрудников.

    Args:
        per (Union[Unset, int]):  Default: 50.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagsResponse200, GetTagsResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            per=per,
            page=page,
        )
    ).parsed
