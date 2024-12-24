import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_chats_availability import GetChatsAvailability
from ...models.get_chats_response_200 import GetChatsResponse200
from ...models.get_chats_response_400 import GetChatsResponse400
from ...models.get_chats_response_404 import GetChatsResponse404
from ...models.get_chats_response_422 import GetChatsResponse422
from ...models.get_chats_sortid import GetChatsSortid
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sortid: Union[Unset, GetChatsSortid] = GetChatsSortid.DESC,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    availability: Union[Unset, GetChatsAvailability] = GetChatsAvailability.IS_MEMBER,
    last_message_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_at_before: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_sortid: Union[Unset, str] = UNSET
    if not isinstance(sortid, Unset):
        json_sortid = sortid.value

    params["sort[id]"] = json_sortid

    params["per"] = per

    params["page"] = page

    json_availability: Union[Unset, str] = UNSET
    if not isinstance(availability, Unset):
        json_availability = availability.value

    params["availability"] = json_availability

    json_last_message_at_after: Union[Unset, str] = UNSET
    if not isinstance(last_message_at_after, Unset):
        json_last_message_at_after = last_message_at_after.isoformat()
    params["last_message_at_after"] = json_last_message_at_after

    json_last_message_at_before: Union[Unset, str] = UNSET
    if not isinstance(last_message_at_before, Unset):
        json_last_message_at_before = last_message_at_before.isoformat()
    params["last_message_at_before"] = json_last_message_at_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
    if response.status_code == 200:
        response_200 = GetChatsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetChatsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = GetChatsResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = GetChatsResponse422.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sortid: Union[Unset, GetChatsSortid] = GetChatsSortid.DESC,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    availability: Union[Unset, GetChatsAvailability] = GetChatsAvailability.IS_MEMBER,
    last_message_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_at_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
    """Список бесед и каналов

     Получения списка бесед и каналов по заданным параметрам.

    Args:
        sortid (Union[Unset, GetChatsSortid]):  Default: GetChatsSortid.DESC.
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        availability (Union[Unset, GetChatsAvailability]):  Default:
            GetChatsAvailability.IS_MEMBER.
        last_message_at_after (Union[Unset, datetime.datetime]):
        last_message_at_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]
    """

    kwargs = _get_kwargs(
        sortid=sortid,
        per=per,
        page=page,
        availability=availability,
        last_message_at_after=last_message_at_after,
        last_message_at_before=last_message_at_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sortid: Union[Unset, GetChatsSortid] = GetChatsSortid.DESC,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    availability: Union[Unset, GetChatsAvailability] = GetChatsAvailability.IS_MEMBER,
    last_message_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_at_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
    """Список бесед и каналов

     Получения списка бесед и каналов по заданным параметрам.

    Args:
        sortid (Union[Unset, GetChatsSortid]):  Default: GetChatsSortid.DESC.
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        availability (Union[Unset, GetChatsAvailability]):  Default:
            GetChatsAvailability.IS_MEMBER.
        last_message_at_after (Union[Unset, datetime.datetime]):
        last_message_at_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]
    """

    return sync_detailed(
        client=client,
        sortid=sortid,
        per=per,
        page=page,
        availability=availability,
        last_message_at_after=last_message_at_after,
        last_message_at_before=last_message_at_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sortid: Union[Unset, GetChatsSortid] = GetChatsSortid.DESC,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    availability: Union[Unset, GetChatsAvailability] = GetChatsAvailability.IS_MEMBER,
    last_message_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_at_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
    """Список бесед и каналов

     Получения списка бесед и каналов по заданным параметрам.

    Args:
        sortid (Union[Unset, GetChatsSortid]):  Default: GetChatsSortid.DESC.
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        availability (Union[Unset, GetChatsAvailability]):  Default:
            GetChatsAvailability.IS_MEMBER.
        last_message_at_after (Union[Unset, datetime.datetime]):
        last_message_at_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]
    """

    kwargs = _get_kwargs(
        sortid=sortid,
        per=per,
        page=page,
        availability=availability,
        last_message_at_after=last_message_at_after,
        last_message_at_before=last_message_at_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def getChats(
    *,
    client: Union[AuthenticatedClient, Client],
    sortid: Union[Unset, GetChatsSortid] = GetChatsSortid.DESC,
    per: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    availability: Union[Unset, GetChatsAvailability] = GetChatsAvailability.IS_MEMBER,
    last_message_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_at_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
    """Список бесед и каналов

     Получения списка бесед и каналов по заданным параметрам.

    Args:
        sortid (Union[Unset, GetChatsSortid]):  Default: GetChatsSortid.DESC.
        per (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        availability (Union[Unset, GetChatsAvailability]):  Default:
            GetChatsAvailability.IS_MEMBER.
        last_message_at_after (Union[Unset, datetime.datetime]):
        last_message_at_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]
    """

    return (
        await asyncio_detailed(
            client=client,
            sortid=sortid,
            per=per,
            page=page,
            availability=availability,
            last_message_at_after=last_message_at_after,
            last_message_at_before=last_message_at_before,
        )
    ).parsed
