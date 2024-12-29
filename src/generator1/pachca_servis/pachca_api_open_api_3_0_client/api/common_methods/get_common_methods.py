from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.bad_request import BadRequest
from ...models.get_common_methods_response_200 import GetCommonMethodsResponse200
from ...types import UNSET, Response


def _get_kwargs_getCommonMethods(
    self,
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


def _parse_response_getCommonMethods(
    self, response: httpx.Response
) -> Optional[Union[BadRequest, GetCommonMethodsResponse200]]:
    if response.status_code == 200:
        response_200 = GetCommonMethodsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getCommonMethods(
    self, response: httpx.Response
) -> Response[Union[BadRequest, GetCommonMethodsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getCommonMethods(response=response),
    )


async def getCommonMethods(
    self,
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

    kwargs = self._get_kwargs_getCommonMethods(
        entity_type=entity_type,
    )

    response = await self.client.get_async_httpx_client().request(**kwargs)

    return self._build_response_getCommonMethods(response=response).parsed
