from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...models.errors_code import ErrorsCode
from ...models.post_members_to_chats_body import PostMembersToChatsBody
from ...types import Response
from .client_serv import HttpClient


def _get_kwargs_postMembersToChats(
    self,
    id: int,
    body: PostMembersToChatsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/chats/{id}/members",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response_postMembersToChats(self, response: httpx.Response) -> Optional[Union[Any, list["ErrorsCode"]]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ErrorsCode.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_postMembersToChats(self, response: httpx.Response) -> Response[Union[Any, list["ErrorsCode"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_postMembersToChats(response=response),
    )


async def postMembersToChats(
    self,
    id: int,
    body: PostMembersToChatsBody,
) -> Optional[Union[Any, list["ErrorsCode"]]]:
    """добавление пользователей в состав участников

     Метод для добавления пользователей в состав участников беседы или канала.

    Args:
        id (int):  Example: 533.
        body (PostMembersToChatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ErrorsCode']]
    """

    kwargs = self._get_kwargs_postMembersToChats(
        id=id,
        body=body,
    )

    # response = await self.client.get_async_httpx_client().request(
    #    **kwargs
    # )
    response = await HttpClient.request(
        method=kwargs["method"], url=kwargs["url"], **kwargs
    )  # Используйте статичный метод

    return self._build_response_postMembersToChats(response=response).parsed
