from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.edit_message_body import EditMessageBody
from ...models.edit_message_response_200 import EditMessageResponse200
from ...models.errors_code import ErrorsCode
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_editMessage(
    self,
    id: int,
    body: EditMessageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/messages/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response_editMessage(
    self, response: httpx.Response
) -> Optional[Union[EditMessageResponse200, list["ErrorsCode"]]]:
    if response.status_code == 200:
        response_200 = EditMessageResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ErrorsCode.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400
    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ErrorsCode.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_editMessage(
    self, response: httpx.Response
) -> Response[Union[EditMessageResponse200, list["ErrorsCode"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_editMessage(response=response),
    )


async def editMessage(
    self,
    id: int,
    body: EditMessageBody,
) -> Optional[Union[EditMessageResponse200, list["ErrorsCode"]]]:
    """Редактирование сообщения

     Метод для редактирования сообщения или комментария.

    Args:
        id (int):
        body (EditMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EditMessageResponse200, list['ErrorsCode']]
    """

    kwargs = self._get_kwargs_editMessage(
        id=id,
        body=body,
    )

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_editMessage(response=response).parsed
