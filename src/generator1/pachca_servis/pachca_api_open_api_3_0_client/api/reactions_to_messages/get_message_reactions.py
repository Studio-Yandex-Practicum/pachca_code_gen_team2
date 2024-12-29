from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...models.bad_request import BadRequest
from ...models.get_message_reactions_body import GetMessageReactionsBody
from ...models.get_message_reactions_response_200 import GetMessageReactionsResponse200
from ...models.not_found import NotFound
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_getMessageReactions(
    self,
    id: int,
    body: GetMessageReactionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/messages/{id}/reactions",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response_getMessageReactions(
    self, response: httpx.Response
) -> Optional[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
    if response.status_code == 200:
        response_200 = GetMessageReactionsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if response.status_code == 400:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getMessageReactions(
    self, response: httpx.Response
) -> Response[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getMessageReactions(response=response),
    )


async def getMessageReactions(
    self,
    id: int,
    body: GetMessageReactionsBody,
) -> Optional[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
    """Получение актуального списка реакций.

     Этот метод позволяет получить список всех реакций, оставленных пользователями на указанное
    сообщение.

    Args:
        id (int):
        body (GetMessageReactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetMessageReactionsResponse200, NotFound]
    """

    kwargs = self._get_kwargs_getMessageReactions(
        id=id,
        body=body,
    )

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_getMessageReactions(response=response).parsed
