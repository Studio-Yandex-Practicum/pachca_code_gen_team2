from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_code import ErrorsCode
from ...models.post_tags_to_chats_body import PostTagsToChatsBody
from ...types import Response


def _get_kwargs_postTagsToChats(
    self,
    id: int,
    *,
    body: PostTagsToChatsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/chats/{id}/group_tags",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response_postTagsToChats(
    self, *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ErrorsCode"]]]:
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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_postTagsToChats(
    self, *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["ErrorsCode"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_postTagsToChats(client=client, response=response),
    )


async def asyncio_detailed_postTagsToChats(
    self,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostTagsToChatsBody,
) -> Response[Union[Any, list["ErrorsCode"]]]:
    """добавление тегов в состав участников беседы или канала

     Метод для добавления тегов в состав участников беседы или канала.

    Args:
        id (int):  Example: 533.
        body (PostTagsToChatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ErrorsCode']]]
    """

    kwargs = self._get_kwargs_postTagsToChats(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return self._build_response_postTagsToChats(client=client, response=response)


async def postTagsToChats(
    self,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostTagsToChatsBody,
) -> Optional[Union[Any, list["ErrorsCode"]]]:
    """добавление тегов в состав участников беседы или канала

     Метод для добавления тегов в состав участников беседы или канала.

    Args:
        id (int):  Example: 533.
        body (PostTagsToChatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ErrorsCode']]
    """

    return (
        await self.asyncio_detailed_postTagsToChats(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
