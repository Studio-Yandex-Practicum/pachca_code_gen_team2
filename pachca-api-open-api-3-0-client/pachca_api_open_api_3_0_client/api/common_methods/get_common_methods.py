from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.get_common_methods_response_200 import GetCommonMethodsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    entity_type: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["entity_type"] = entity_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/custom_properties",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, GetCommonMethodsResponse200]]:
    if response.status_code == 200:
        response_200 = GetCommonMethodsResponse200.from_dict(response.json())

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
) -> Response[Union[BadRequest, GetCommonMethodsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: str,
) -> Response[Union[BadRequest, GetCommonMethodsResponse200]]:
    """Список дополнительных полей

     Метод для получения актуального списка дополнительных полей участников и напоминаний в вашей
    компании.

    Args:
        entity_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetCommonMethodsResponse200]]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: str,
) -> Optional[Union[BadRequest, GetCommonMethodsResponse200]]:
    """Список дополнительных полей

     Метод для получения актуального списка дополнительных полей участников и напоминаний в вашей
    компании.

    Args:
        entity_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetCommonMethodsResponse200]
    """

    return sync_detailed(
        client=client,
        entity_type=entity_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: str,
) -> Response[Union[BadRequest, GetCommonMethodsResponse200]]:
    """Список дополнительных полей

     Метод для получения актуального списка дополнительных полей участников и напоминаний в вашей
    компании.

    Args:
        entity_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetCommonMethodsResponse200]]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getCommonMethods(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: str,
) -> Optional[Union[BadRequest, GetCommonMethodsResponse200]]:
    """Список дополнительных полей

     Метод для получения актуального списка дополнительных полей участников и напоминаний в вашей
    компании.

    Args:
        entity_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetCommonMethodsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            entity_type=entity_type,
        )
    ).parsed
