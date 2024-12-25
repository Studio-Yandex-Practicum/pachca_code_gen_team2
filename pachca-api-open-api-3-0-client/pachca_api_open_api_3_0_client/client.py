from .models.get_chats_response_422 import GetChatsResponse422
from .models.get_message_reactions_response_200 import GetMessageReactionsResponse200
from http import HTTPStatus
from .models.post_message_reactions_body import PostMessageReactionsBody
from .models.create_chat_response_422 import CreateChatResponse422
from .models.post_tasks_body import PostTasksBody
from .models.create_message_response_201 import CreateMessageResponse201
from .models.get_tags_response_200 import GetTagsResponse200
from .models.get_tags_response_400 import GetTagsResponse400
from .models.create_chat_body import CreateChatBody
from .models.post_message_reactions_response_403 import PostMessageReactionsResponse403
from .models.get_employees_response_200 import GetEmployeesResponse200
from .models.get_tag_response_200 import GetTagResponse200
from .models.get_chats_sortid import GetChatsSortid
from .types import UNSET
from .models.get_status_response_200 import GetStatusResponse200
from .models.delete_message_reactions_response_404 import DeleteMessageReactionsResponse404
from .models.get_tags_employees_response_200 import GetTagsEmployeesResponse200
from .models.put_status_response_201 import PutStatusResponse201
from .models.errors_code import ErrorsCode
from .models.direct_response import DirectResponse
from .models.put_messages_id_response_200 import PutMessagesIdResponse200
from .models.get_list_message_response_200 import GetListMessageResponse200
from .models.post_members_to_chats_body import PostMembersToChatsBody
from .models.file_response import FileResponse
from .models.get_employee_response_200 import GetEmployeeResponse200
from .models.create_thread_response_200 import CreateThreadResponse200
from . import errors
from .models.bad_request import BadRequest
from .models.create_chat_response_404 import CreateChatResponse404
from .models.put_messages_id_body import PutMessagesIdBody
from .models.get_tag_response_404 import GetTagResponse404
from .models.get_message_reactions_body import GetMessageReactionsBody
from .models.create_message_body import CreateMessageBody
from .models.get_chats_availability import GetChatsAvailability
from .models.post_message_reactions_response_400 import PostMessageReactionsResponse400
from .models.get_chats_response_400 import GetChatsResponse400
from .models.get_common_methods_response_200 import GetCommonMethodsResponse200
from .models.post_tags_to_chats_body import PostTagsToChatsBody
from .models.get_chat_response_404 import GetChatResponse404
from typing import Union
from .models.get_chat_response_200 import GetChatResponse200
from .models.create_chat_response_400 import CreateChatResponse400
from .models.get_chats_response_404 import GetChatsResponse404
from .models.create_chat_response_201 import CreateChatResponse201
from .models.query_status import QueryStatus
from .models.delete_message_reactions_response_400 import DeleteMessageReactionsResponse400
from typing import cast
from .models.error import Error
from .models.post_tasks_response_201 import PostTasksResponse201
from .models.not_found import NotFound
from .models.post_tasks_response_400 import PostTasksResponse400
from .models.get_message_response_200 import GetMessageResponse200
from .models.get_chats_response_200 import GetChatsResponse200
from .types import Response
from .models.post_message_reactions_response_404 import PostMessageReactionsResponse404
from typing import Any
from typing import Optional
from .types import Unset

import datetime
import ssl
from typing import Any, Union, Optional

from attrs import define, field, evolve
import httpx



@define
class Client:
    """A class for keeping track of data related to the API



    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
    """

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(alias="base_url")
    _cookies: dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: Optional[httpx.Timeout] = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: Union[str, bool, ssl.SSLContext] = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)


    def with_headers(self, headers: dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)


    def set_httpx_client(self, client: httpx.Client) -> "Client":
        """Manually set the underlying httpx.Client

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
        
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "Client":
        """Enter a context manager for self.client—you cannot enter twice (see httpx docs)"""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client (see httpx docs)"""
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "Client":
        """Manually the underlying httpx.AsyncClient

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
        
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "Client":
        """Enter a context manager for underlying httpx.AsyncClient—you cannot enter twice (see httpx docs)"""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)


@define
class AuthenticatedClient:
    """A Client which has been authenticated for use on secured endpoints

    
    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    """

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(alias="base_url")
    _cookies: dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: Optional[httpx.Timeout] = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: Union[str, bool, ssl.SSLContext] = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def with_headers(self, headers: dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "AuthenticatedClient":
        """Get a new client matching this one with a new timeout (in seconds)"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    def set_httpx_client(self, client: httpx.Client) -> "AuthenticatedClient":
        """Manually set the underlying httpx.Client

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "AuthenticatedClient":
        """Enter a context manager for self.client—you cannot enter twice (see httpx docs)"""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client (see httpx docs)"""
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "AuthenticatedClient":
        """Manually the underlying httpx.AsyncClient

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "AuthenticatedClient":
        """Enter a context manager for underlying httpx.AsyncClient—you cannot enter twice (see httpx docs)"""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)


class Pachca:
    """Главный класс библиотеки."""

    def __init__(self, base_url, token):
        self.client = AuthenticatedClient(base_url=base_url, token=token)

    
    
    def _get_kwargs_createThread(self, id: int) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'post', 'url': f'/messages/{id}/thread'}
        return _kwargs
    
    def _parse_response_createThread(self, response: httpx.Response) -> Optional[Union[BadRequest, CreateThreadResponse200, NotFound]]:
        if response.status_code == 200:
            response_200 = CreateThreadResponse200.from_dict(response.json())
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
    
    def _build_response_createThread(self, response: httpx.Response) -> Response[Union[BadRequest, CreateThreadResponse200, NotFound]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_createThread(response=response))
    
    async def asyncio_detailed_createThread(self, id: int) -> Response[Union[BadRequest, CreateThreadResponse200, NotFound]]:
        """Создание нового треда

         Этот метод позволяет создать новый тред к сообщению. Если у сообщения уже был создан тред, то в
        ответе вернётся информация об уже созданном ранее треде.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[BadRequest, CreateThreadResponse200, NotFound]]
        """
        kwargs = self._get_kwargs_createThread(id=id)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_createThread(response=response)
    
    async def createThread(self, id: int) -> Optional[Union[BadRequest, CreateThreadResponse200, NotFound]]:
        """Создание нового треда

         Этот метод позволяет создать новый тред к сообщению. Если у сообщения уже был создан тред, то в
        ответе вернётся информация об уже созданном ранее треде.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[BadRequest, CreateThreadResponse200, NotFound]
        """
        return (await self.asyncio_detailed_createThread(id=id)).parsed
    
    def _get_kwargs_getCommonMethods(self, entity_type: str) -> dict[str, Any]:
        params: dict[str, Any] = {}
        params['entity_type'] = entity_type
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': '/custom_properties', 'params': params}
        return _kwargs
    
    def _parse_response_getCommonMethods(self, response: httpx.Response) -> Optional[Union[BadRequest, GetCommonMethodsResponse200]]:
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
    
    def _build_response_getCommonMethods(self, response: httpx.Response) -> Response[Union[BadRequest, GetCommonMethodsResponse200]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getCommonMethods(response=response))
    
    async def asyncio_detailed_getCommonMethods(self, entity_type: str) -> Response[Union[BadRequest, GetCommonMethodsResponse200]]:
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
        kwargs = self._get_kwargs_getCommonMethods(entity_type=entity_type)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getCommonMethods(response=response)
    
    async def getCommonMethods(self, entity_type: str) -> Optional[Union[BadRequest, GetCommonMethodsResponse200]]:
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
        return (await self.asyncio_detailed_getCommonMethods(entity_type=entity_type)).parsed
    
    def _get_kwargs_getDirectUrl(self, body: DirectResponse) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': '/direct_url'}
        _body = body.to_multipart()
        _kwargs['files'] = _body
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_getDirectUrl(self, response: httpx.Response) -> Optional[Any]:
        if response.status_code == 204:
            return None
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getDirectUrl(self, response: httpx.Response) -> Response[Any]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getDirectUrl(response=response))
    
    async def asyncio_detailed_getDirectUrl(self, body: DirectResponse) -> Response[Any]:
        """Получение URL для загрузки

         Отправляет запрос для получения URL для безопасной загрузки файла.

        Args:
            body (DirectResponse):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """
        kwargs = self._get_kwargs_getDirectUrl(body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getDirectUrl(response=response)
    
    def _get_kwargs_getUploads(self) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'post', 'url': '/uploads'}
        return _kwargs
    
    def _parse_response_getUploads(self, response: httpx.Response) -> Optional[FileResponse]:
        if response.status_code == 200:
            response_200 = FileResponse.from_dict(response.json())
            return response_200
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getUploads(self, response: httpx.Response) -> Response[FileResponse]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getUploads(response=response))
    
    async def asyncio_detailed_getUploads(self) -> Response[FileResponse]:
        """Получение подписи и ключа для загрузки файла

         Возвращает параметры, необходимые для безопасной загрузки файла.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[FileResponse]
        """
        kwargs = self._get_kwargs_getUploads()
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getUploads(response=response)
    
    async def getUploads(self) -> Optional[FileResponse]:
        """Получение подписи и ключа для загрузки файла

         Возвращает параметры, необходимые для безопасной загрузки файла.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            FileResponse
        """
        return (await self.asyncio_detailed_getUploads()).parsed
    
    def _get_kwargs_put_messages_id(self, id: int, body: PutMessagesIdBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'put', 'url': f'/messages/{id}'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_put_messages_id(self, response: httpx.Response) -> Optional[Union[PutMessagesIdResponse200, list['ErrorsCode']]]:
        if response.status_code == 200:
            response_200 = PutMessagesIdResponse200.from_dict(response.json())
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
    
    def _build_response_put_messages_id(self, response: httpx.Response) -> Response[Union[PutMessagesIdResponse200, list['ErrorsCode']]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_put_messages_id(response=response))
    
    async def asyncio_detailed_put_messages_id(self, id: int, body: PutMessagesIdBody) -> Response[Union[PutMessagesIdResponse200, list['ErrorsCode']]]:
        """Редактирование сообщения

         Метод для редактирования сообщения или комментария.

        Args:
            id (int):
            body (PutMessagesIdBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[PutMessagesIdResponse200, list['ErrorsCode']]]
        """
        kwargs = self._get_kwargs_put_messages_id(id=id, body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_put_messages_id(response=response)
    
    async def put_messages_id(self, id: int, body: PutMessagesIdBody) -> Optional[Union[PutMessagesIdResponse200, list['ErrorsCode']]]:
        """Редактирование сообщения

         Метод для редактирования сообщения или комментария.

        Args:
            id (int):
            body (PutMessagesIdBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[PutMessagesIdResponse200, list['ErrorsCode']]
        """
        return (await self.asyncio_detailed_put_messages_id(id=id, body=body)).parsed
    
    def _get_kwargs_createMessage(self, body: CreateMessageBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': '/messages'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_createMessage(self, response: httpx.Response) -> Optional[Union[BadRequest, CreateMessageResponse201, list['Error']]]:
        if response.status_code == 201:
            response_201 = CreateMessageResponse201.from_dict(response.json())
            return response_201
        if response.status_code == 404:
            response_404 = []
            _response_404 = response.json()
            for componentsschemas_errors_item_data in _response_404:
                componentsschemas_errors_item = Error.from_dict(componentsschemas_errors_item_data)
                response_404.append(componentsschemas_errors_item)
            return response_404
        if response.status_code == 400:
            response_400 = BadRequest.from_dict(response.json())
            return response_400
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_createMessage(self, response: httpx.Response) -> Response[Union[BadRequest, CreateMessageResponse201, list['Error']]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_createMessage(response=response))
    
    async def asyncio_detailed_createMessage(self, body: CreateMessageBody) -> Response[Union[BadRequest, CreateMessageResponse201, list['Error']]]:
        """создание нового сообщения

         Метод для отправки сообщения в беседу или канал,
        личного сообщения пользователю или комментария в тред.

        При использовании entity_type: \\"discussion\\" (или просто без указания entity_type)
        допускается отправка любого chat_id в поле entity_id.
        То есть, сообщение можно отправить зная только идентификатор чата.
        При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
        или личное сообщение по идентификатору пользователя.

        Для отправки личного сообщения пользователю создавать чат не требуется.
        Достаточно указать entity_type: \\"user\\" и идентификатор пользователя.
        Чат будет создан автоматически, если между вами ещё не было переписки.
        Между двумя пользователями может быть только один личный чат.

        Args:
            body (CreateMessageBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[BadRequest, CreateMessageResponse201, list['Error']]]
        """
        kwargs = self._get_kwargs_createMessage(body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_createMessage(response=response)
    
    async def createMessage(self, body: CreateMessageBody) -> Optional[Union[BadRequest, CreateMessageResponse201, list['Error']]]:
        """создание нового сообщения

         Метод для отправки сообщения в беседу или канал,
        личного сообщения пользователю или комментария в тред.

        При использовании entity_type: \\"discussion\\" (или просто без указания entity_type)
        допускается отправка любого chat_id в поле entity_id.
        То есть, сообщение можно отправить зная только идентификатор чата.
        При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
        или личное сообщение по идентификатору пользователя.

        Для отправки личного сообщения пользователю создавать чат не требуется.
        Достаточно указать entity_type: \\"user\\" и идентификатор пользователя.
        Чат будет создан автоматически, если между вами ещё не было переписки.
        Между двумя пользователями может быть только один личный чат.

        Args:
            body (CreateMessageBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[BadRequest, CreateMessageResponse201, list['Error']]
        """
        return (await self.asyncio_detailed_createMessage(body=body)).parsed
    
    def _get_kwargs_getMessage(self, id: int) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'get', 'url': f'/messages/{id}'}
        return _kwargs
    
    def _parse_response_getMessage(self, response: httpx.Response) -> Optional[Union[GetMessageResponse200, NotFound]]:
        if response.status_code == 200:
            response_200 = GetMessageResponse200.from_dict(response.json())
            return response_200
        if response.status_code == 404:
            response_404 = NotFound.from_dict(response.json())
            return response_404
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getMessage(self, response: httpx.Response) -> Response[Union[GetMessageResponse200, NotFound]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getMessage(response=response))
    
    async def asyncio_detailed_getMessage(self, id: int) -> Response[Union[GetMessageResponse200, NotFound]]:
        """получение информации о сообщении

         Метод для получения информации о сообщении.

        Для получения сообщения вам необходимо знать его id и указать его в URL запроса.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[GetMessageResponse200, NotFound]]
        """
        kwargs = self._get_kwargs_getMessage(id=id)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getMessage(response=response)
    
    async def getMessage(self, id: int) -> Optional[Union[GetMessageResponse200, NotFound]]:
        """получение информации о сообщении

         Метод для получения информации о сообщении.

        Для получения сообщения вам необходимо знать его id и указать его в URL запроса.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[GetMessageResponse200, NotFound]
        """
        return (await self.asyncio_detailed_getMessage(id=id)).parsed
    
    def _get_kwargs_getListMessage(self, chat_id: int, per: Union[Unset, int]=25, page: Union[Unset, int]=1) -> dict[str, Any]:
        params: dict[str, Any] = {}
        params['chat_id'] = chat_id
        params['per'] = per
        params['page'] = page
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': '/messages', 'params': params}
        return _kwargs
    
    def _parse_response_getListMessage(self, response: httpx.Response) -> Optional[Union[BadRequest, GetListMessageResponse200, NotFound]]:
        if response.status_code == 200:
            response_200 = GetListMessageResponse200.from_dict(response.json())
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
    
    def _build_response_getListMessage(self, response: httpx.Response) -> Response[Union[BadRequest, GetListMessageResponse200, NotFound]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getListMessage(response=response))
    
    async def asyncio_detailed_getListMessage(self, chat_id: int, per: Union[Unset, int]=25, page: Union[Unset, int]=1) -> Response[Union[BadRequest, GetListMessageResponse200, NotFound]]:
        """получение списка сообщений чата

         Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.

        Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
        треда или диалога, и указать его в URL запроса. Сообщения будут возвращены
        в порядке убывания даты отправки (то есть, сначала будут идти последние сообщения чата).
        Для получения более ранних сообщений чата доступны параметры per и page.

        Args:
            chat_id (int):
            per (Union[Unset, int]):  Default: 25.
            page (Union[Unset, int]):  Default: 1.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[BadRequest, GetListMessageResponse200, NotFound]]
        """
        kwargs = self._get_kwargs_getListMessage(chat_id=chat_id, per=per, page=page)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getListMessage(response=response)
    
    async def getListMessage(self, chat_id: int, per: Union[Unset, int]=25, page: Union[Unset, int]=1) -> Optional[Union[BadRequest, GetListMessageResponse200, NotFound]]:
        """получение списка сообщений чата

         Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.

        Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
        треда или диалога, и указать его в URL запроса. Сообщения будут возвращены
        в порядке убывания даты отправки (то есть, сначала будут идти последние сообщения чата).
        Для получения более ранних сообщений чата доступны параметры per и page.

        Args:
            chat_id (int):
            per (Union[Unset, int]):  Default: 25.
            page (Union[Unset, int]):  Default: 1.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[BadRequest, GetListMessageResponse200, NotFound]
        """
        return (await self.asyncio_detailed_getListMessage(chat_id=chat_id, per=per, page=page)).parsed
    
    def _get_kwargs_postTagsToChats(self, id: int, body: PostTagsToChatsBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': f'/chats/{id}/group_tags'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_postTagsToChats(self, response: httpx.Response) -> Optional[Union[Any, list['ErrorsCode']]]:
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
    
    def _build_response_postTagsToChats(self, response: httpx.Response) -> Response[Union[Any, list['ErrorsCode']]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_postTagsToChats(response=response))
    
    async def asyncio_detailed_postTagsToChats(self, id: int, body: PostTagsToChatsBody) -> Response[Union[Any, list['ErrorsCode']]]:
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
        kwargs = self._get_kwargs_postTagsToChats(id=id, body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_postTagsToChats(response=response)
    
    async def postTagsToChats(self, id: int, body: PostTagsToChatsBody) -> Optional[Union[Any, list['ErrorsCode']]]:
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
        return (await self.asyncio_detailed_postTagsToChats(id=id, body=body)).parsed
    
    def _get_kwargs_delete_chats_id_leave(self, id: int) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'delete', 'url': f'/chats/{id}/leave'}
        return _kwargs
    
    def _parse_response_delete_chats_id_leave(self, response: httpx.Response) -> Optional[Union[Any, list['ErrorsCode']]]:
        if response.status_code == 200:
            response_200 = cast(Any, None)
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
    
    def _build_response_delete_chats_id_leave(self, response: httpx.Response) -> Response[Union[Any, list['ErrorsCode']]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_delete_chats_id_leave(response=response))
    
    async def asyncio_detailed_delete_chats_id_leave(self, id: int) -> Response[Union[Any, list['ErrorsCode']]]:
        """Выход из беседы или канала

         Метод для самостоятельного выхода из беседы или канала.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, list['ErrorsCode']]]
        """
        kwargs = self._get_kwargs_delete_chats_id_leave(id=id)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_delete_chats_id_leave(response=response)
    
    async def delete_chats_id_leave(self, id: int) -> Optional[Union[Any, list['ErrorsCode']]]:
        """Выход из беседы или канала

         Метод для самостоятельного выхода из беседы или канала.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, list['ErrorsCode']]
        """
        return (await self.asyncio_detailed_delete_chats_id_leave(id=id)).parsed
    
    def _get_kwargs_postMembersToChats(self, id: int, body: PostMembersToChatsBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': f'/chats/{id}/members'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_postMembersToChats(self, response: httpx.Response) -> Optional[Union[Any, list['ErrorsCode']]]:
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
    
    def _build_response_postMembersToChats(self, response: httpx.Response) -> Response[Union[Any, list['ErrorsCode']]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_postMembersToChats(response=response))
    
    async def asyncio_detailed_postMembersToChats(self, id: int, body: PostMembersToChatsBody) -> Response[Union[Any, list['ErrorsCode']]]:
        """добавление пользователей в состав участников

         Метод для добавления пользователей в состав участников беседы или канала.

        Args:
            id (int):  Example: 533.
            body (PostMembersToChatsBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, list['ErrorsCode']]]
        """
        kwargs = self._get_kwargs_postMembersToChats(id=id, body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_postMembersToChats(response=response)
    
    async def postMembersToChats(self, id: int, body: PostMembersToChatsBody) -> Optional[Union[Any, list['ErrorsCode']]]:
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
        return (await self.asyncio_detailed_postMembersToChats(id=id, body=body)).parsed
    
    def _get_kwargs_getChat(self, id: int) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'get', 'url': f'/chats/{id}'}
        return _kwargs
    
    def _parse_response_getChat(self, response: httpx.Response) -> Optional[Union[GetChatResponse200, GetChatResponse404]]:
        if response.status_code == 200:
            response_200 = GetChatResponse200.from_dict(response.json())
            return response_200
        if response.status_code == 404:
            response_404 = GetChatResponse404.from_dict(response.json())
            return response_404
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getChat(self, response: httpx.Response) -> Response[Union[GetChatResponse200, GetChatResponse404]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getChat(response=response))
    
    async def asyncio_detailed_getChat(self, id: int) -> Response[Union[GetChatResponse200, GetChatResponse404]]:
        """Информация о беседе или канале

         Получения информации о беседе или канале.
        Для получения беседы или канала вам необходимо знать её id и указать его в URL запроса.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[GetChatResponse200, GetChatResponse404]]
        """
        kwargs = self._get_kwargs_getChat(id=id)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getChat(response=response)
    
    async def getChat(self, id: int) -> Optional[Union[GetChatResponse200, GetChatResponse404]]:
        """Информация о беседе или канале

         Получения информации о беседе или канале.
        Для получения беседы или канала вам необходимо знать её id и указать его в URL запроса.

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[GetChatResponse200, GetChatResponse404]
        """
        return (await self.asyncio_detailed_getChat(id=id)).parsed
    
    def _get_kwargs_createChat(self, body: CreateChatBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': '/chats'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_createChat(self, response: httpx.Response) -> Optional[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
        if response.status_code == 201:
            response_201 = CreateChatResponse201.from_dict(response.json())
            return response_201
        if response.status_code == 400:
            response_400 = CreateChatResponse400.from_dict(response.json())
            return response_400
        if response.status_code == 404:
            response_404 = CreateChatResponse404.from_dict(response.json())
            return response_404
        if response.status_code == 422:
            response_422 = CreateChatResponse422.from_dict(response.json())
            return response_422
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_createChat(self, response: httpx.Response) -> Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_createChat(response=response))
    
    async def asyncio_detailed_createChat(self, body: CreateChatBody) -> Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
        """ Новая беседа или канал

         Метод для создания новой беседы или нового канала.
        При создании беседы или канала вы автоматически становитесь участником.\\

        Args:
            body (CreateChatBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]
         """
        kwargs = self._get_kwargs_createChat(body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_createChat(response=response)
    
    async def createChat(self, body: CreateChatBody) -> Optional[Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]]:
        """ Новая беседа или канал

         Метод для создания новой беседы или нового канала.
        При создании беседы или канала вы автоматически становитесь участником.\\

        Args:
            body (CreateChatBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[CreateChatResponse201, CreateChatResponse400, CreateChatResponse404, CreateChatResponse422]
         """
        return (await self.asyncio_detailed_createChat(body=body)).parsed
    
    def _get_kwargs_getChats(self, sortid: Union[Unset, GetChatsSortid]=GetChatsSortid.DESC, per: Union[Unset, int]=25, page: Union[Unset, int]=1, availability: Union[Unset, GetChatsAvailability]=GetChatsAvailability.IS_MEMBER, last_message_at_after: Union[Unset, datetime.datetime]=UNSET, last_message_at_before: Union[Unset, datetime.datetime]=UNSET) -> dict[str, Any]:
        params: dict[str, Any] = {}
        json_sortid: Union[Unset, str] = UNSET
        if not isinstance(sortid, Unset):
            json_sortid = sortid.value
        params['sort[id]'] = json_sortid
        params['per'] = per
        params['page'] = page
        json_availability: Union[Unset, str] = UNSET
        if not isinstance(availability, Unset):
            json_availability = availability.value
        params['availability'] = json_availability
        json_last_message_at_after: Union[Unset, str] = UNSET
        if not isinstance(last_message_at_after, Unset):
            json_last_message_at_after = last_message_at_after.isoformat()
        params['last_message_at_after'] = json_last_message_at_after
        json_last_message_at_before: Union[Unset, str] = UNSET
        if not isinstance(last_message_at_before, Unset):
            json_last_message_at_before = last_message_at_before.isoformat()
        params['last_message_at_before'] = json_last_message_at_before
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': '/chats', 'params': params}
        return _kwargs
    
    def _parse_response_getChats(self, response: httpx.Response) -> Optional[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
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
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getChats(self, response: httpx.Response) -> Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getChats(response=response))
    
    async def asyncio_detailed_getChats(self, sortid: Union[Unset, GetChatsSortid]=GetChatsSortid.DESC, per: Union[Unset, int]=25, page: Union[Unset, int]=1, availability: Union[Unset, GetChatsAvailability]=GetChatsAvailability.IS_MEMBER, last_message_at_after: Union[Unset, datetime.datetime]=UNSET, last_message_at_before: Union[Unset, datetime.datetime]=UNSET) -> Response[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
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
        kwargs = self._get_kwargs_getChats(sortid=sortid, per=per, page=page, availability=availability, last_message_at_after=last_message_at_after, last_message_at_before=last_message_at_before)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getChats(response=response)
    
    async def getChats(self, sortid: Union[Unset, GetChatsSortid]=GetChatsSortid.DESC, per: Union[Unset, int]=25, page: Union[Unset, int]=1, availability: Union[Unset, GetChatsAvailability]=GetChatsAvailability.IS_MEMBER, last_message_at_after: Union[Unset, datetime.datetime]=UNSET, last_message_at_before: Union[Unset, datetime.datetime]=UNSET) -> Optional[Union[GetChatsResponse200, GetChatsResponse400, GetChatsResponse404, GetChatsResponse422]]:
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
        return (await self.asyncio_detailed_getChats(sortid=sortid, per=per, page=page, availability=availability, last_message_at_after=last_message_at_after, last_message_at_before=last_message_at_before)).parsed
    
    def _get_kwargs_getStatus(self) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'get', 'url': '/profile/status'}
        return _kwargs
    
    def _parse_response_getStatus(self, response: httpx.Response) -> Optional[GetStatusResponse200]:
        if response.status_code == 200:
            response_200 = GetStatusResponse200.from_dict(response.json())
            return response_200
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getStatus(self, response: httpx.Response) -> Response[GetStatusResponse200]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getStatus(response=response))
    
    async def asyncio_detailed_getStatus(self) -> Response[GetStatusResponse200]:
        """получение информации о своем статусе

         Параметры запроса отсутствуют

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[GetStatusResponse200]
        """
        kwargs = self._get_kwargs_getStatus()
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getStatus(response=response)
    
    async def getStatus(self) -> Optional[GetStatusResponse200]:
        """получение информации о своем статусе

         Параметры запроса отсутствуют

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            GetStatusResponse200
        """
        return (await self.asyncio_detailed_getStatus()).parsed
    
    def _get_kwargs_putStatus(self, body: QueryStatus) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'put', 'url': '/profile/status'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_putStatus(self, response: httpx.Response) -> Optional[Union[BadRequest, PutStatusResponse201]]:
        if response.status_code == 201:
            response_201 = PutStatusResponse201.from_dict(response.json())
            return response_201
        if response.status_code == 400:
            response_400 = BadRequest.from_dict(response.json())
            return response_400
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_putStatus(self, response: httpx.Response) -> Response[Union[BadRequest, PutStatusResponse201]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_putStatus(response=response))
    
    async def asyncio_detailed_putStatus(self, body: QueryStatus) -> Response[Union[BadRequest, PutStatusResponse201]]:
        """новый статус

         Создание нового статуса.

        Args:
            body (QueryStatus):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[BadRequest, PutStatusResponse201]]
        """
        kwargs = self._get_kwargs_putStatus(body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_putStatus(response=response)
    
    async def putStatus(self, body: QueryStatus) -> Optional[Union[BadRequest, PutStatusResponse201]]:
        """новый статус

         Создание нового статуса.

        Args:
            body (QueryStatus):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[BadRequest, PutStatusResponse201]
        """
        return (await self.asyncio_detailed_putStatus(body=body)).parsed
    
    def _get_kwargs_delStatus(self) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'delete', 'url': '/profile/status'}
        return _kwargs
    
    def _parse_response_delStatus(self, response: httpx.Response) -> Optional[Any]:
        if response.status_code == 204:
            return None
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_delStatus(self, response: httpx.Response) -> Response[Any]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_delStatus(response=response))
    
    async def asyncio_detailed_delStatus(self) -> Response[Any]:
        """удаление своего статуса

         Параметры запроса отсутствуют

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """
        kwargs = self._get_kwargs_delStatus()
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_delStatus(response=response)
    
    def _get_kwargs_getTags(self, per: Union[Unset, int]=50, page: Union[Unset, int]=1) -> dict[str, Any]:
        params: dict[str, Any] = {}
        params['per'] = per
        params['page'] = page
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': '/group_tags', 'params': params}
        return _kwargs
    
    def _parse_response_getTags(self, response: httpx.Response) -> Optional[Union[GetTagsResponse200, GetTagsResponse400]]:
        if response.status_code == 200:
            response_200 = GetTagsResponse200.from_dict(response.json())
            return response_200
        if response.status_code == 400:
            response_400 = GetTagsResponse400.from_dict(response.json())
            return response_400
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getTags(self, response: httpx.Response) -> Response[Union[GetTagsResponse200, GetTagsResponse400]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getTags(response=response))
    
    async def asyncio_detailed_getTags(self, per: Union[Unset, int]=50, page: Union[Unset, int]=1) -> Response[Union[GetTagsResponse200, GetTagsResponse400]]:
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
        kwargs = self._get_kwargs_getTags(per=per, page=page)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getTags(response=response)
    
    async def getTags(self, per: Union[Unset, int]=50, page: Union[Unset, int]=1) -> Optional[Union[GetTagsResponse200, GetTagsResponse400]]:
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
        return (await self.asyncio_detailed_getTags(per=per, page=page)).parsed
    
    def _get_kwargs_getTag(self, id: int) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'get', 'url': f'/group_tags/{id}'}
        return _kwargs
    
    def _parse_response_getTag(self, response: httpx.Response) -> Optional[Union[GetTagResponse200, GetTagResponse404]]:
        if response.status_code == 200:
            response_200 = GetTagResponse200.from_dict(response.json())
            return response_200
        if response.status_code == 404:
            response_404 = GetTagResponse404.from_dict(response.json())
            return response_404
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getTag(self, response: httpx.Response) -> Response[Union[GetTagResponse200, GetTagResponse404]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getTag(response=response))
    
    async def asyncio_detailed_getTag(self, id: int) -> Response[Union[GetTagResponse200, GetTagResponse404]]:
        """Информация о теге

         Параметры запроса отсутствуют

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[GetTagResponse200, GetTagResponse404]]
        """
        kwargs = self._get_kwargs_getTag(id=id)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getTag(response=response)
    
    async def getTag(self, id: int) -> Optional[Union[GetTagResponse200, GetTagResponse404]]:
        """Информация о теге

         Параметры запроса отсутствуют

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[GetTagResponse200, GetTagResponse404]
        """
        return (await self.asyncio_detailed_getTag(id=id)).parsed
    
    def _get_kwargs_getTagsEmployees(self, id: int, per: Union[Unset, int]=25, page: Union[Unset, int]=1) -> dict[str, Any]:
        params: dict[str, Any] = {}
        params['per'] = per
        params['page'] = page
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': f'/group_tags/{id}/users', 'params': params}
        return _kwargs
    
    def _parse_response_getTagsEmployees(self, response: httpx.Response) -> Optional[Union[BadRequest, GetTagsEmployeesResponse200]]:
        if response.status_code == 200:
            response_200 = GetTagsEmployeesResponse200.from_dict(response.json())
            return response_200
        if response.status_code == 400:
            response_400 = BadRequest.from_dict(response.json())
            return response_400
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getTagsEmployees(self, response: httpx.Response) -> Response[Union[BadRequest, GetTagsEmployeesResponse200]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getTagsEmployees(response=response))
    
    async def asyncio_detailed_getTagsEmployees(self, id: int, per: Union[Unset, int]=25, page: Union[Unset, int]=1) -> Response[Union[BadRequest, GetTagsEmployeesResponse200]]:
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
        kwargs = self._get_kwargs_getTagsEmployees(id=id, per=per, page=page)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getTagsEmployees(response=response)
    
    async def getTagsEmployees(self, id: int, per: Union[Unset, int]=25, page: Union[Unset, int]=1) -> Optional[Union[BadRequest, GetTagsEmployeesResponse200]]:
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
        return (await self.asyncio_detailed_getTagsEmployees(id=id, per=per, page=page)).parsed
    
    def _get_kwargs_post_tasks(self, body: PostTasksBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': '/tasks'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_post_tasks(self, response: httpx.Response) -> Optional[Union[PostTasksResponse201, PostTasksResponse400]]:
        if response.status_code == 201:
            response_201 = PostTasksResponse201.from_dict(response.json())
            return response_201
        if response.status_code == 400:
            response_400 = PostTasksResponse400.from_dict(response.json())
            return response_400
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_post_tasks(self, response: httpx.Response) -> Response[Union[PostTasksResponse201, PostTasksResponse400]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_post_tasks(response=response))
    
    async def asyncio_detailed_post_tasks(self, body: PostTasksBody) -> Response[Union[PostTasksResponse201, PostTasksResponse400]]:
        """Метод для создания нового напоминания.

         При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
        простое напоминание, событие или письмо.
        При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
        текстом.
        Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
        У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

        Args:
            body (PostTasksBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[PostTasksResponse201, PostTasksResponse400]]
        """
        kwargs = self._get_kwargs_post_tasks(body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_post_tasks(response=response)
    
    async def post_tasks(self, body: PostTasksBody) -> Optional[Union[PostTasksResponse201, PostTasksResponse400]]:
        """Метод для создания нового напоминания.

         При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча,
        простое напоминание, событие или письмо.
        При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим
        текстом.
        Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
        У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.

        Args:
            body (PostTasksBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[PostTasksResponse201, PostTasksResponse400]
        """
        return (await self.asyncio_detailed_post_tasks(body=body)).parsed
    
    def _get_kwargs_postMessageReactions(self, id: str, body: PostMessageReactionsBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'post', 'url': f'/messages/{id}/reactions'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_postMessageReactions(self, response: httpx.Response) -> Optional[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]:
        if response.status_code == 204:
            response_204 = cast(Any, None)
            return response_204
        if response.status_code == 400:
            response_400 = PostMessageReactionsResponse400.from_dict(response.json())
            return response_400
        if response.status_code == 403:
            response_403 = PostMessageReactionsResponse403.from_dict(response.json())
            return response_403
        if response.status_code == 404:
            response_404 = PostMessageReactionsResponse404.from_dict(response.json())
            return response_404
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_postMessageReactions(self, response: httpx.Response) -> Response[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_postMessageReactions(response=response))
    
    async def asyncio_detailed_postMessageReactions(self, id: str, body: PostMessageReactionsBody) -> Response[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]:
        """Добавление реакции

         Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый пользователь может
        установить не более 20 уникальных реакций на сообщение. - Сообщение может иметь не более 30
        уникальных реакций. - Сообщение может иметь не более 1000 реакций.

        Args:
            id (str):
            body (PostMessageReactionsBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]
        """
        kwargs = self._get_kwargs_postMessageReactions(id=id, body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_postMessageReactions(response=response)
    
    async def postMessageReactions(self, id: str, body: PostMessageReactionsBody) -> Optional[Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]]:
        """Добавление реакции

         Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый пользователь может
        установить не более 20 уникальных реакций на сообщение. - Сообщение может иметь не более 30
        уникальных реакций. - Сообщение может иметь не более 1000 реакций.

        Args:
            id (str):
            body (PostMessageReactionsBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, PostMessageReactionsResponse400, PostMessageReactionsResponse403, PostMessageReactionsResponse404]
        """
        return (await self.asyncio_detailed_postMessageReactions(id=id, body=body)).parsed
    
    def _get_kwargs_getMessageReactions(self, id: int, body: GetMessageReactionsBody) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': f'/messages/{id}/reactions'}
        _body = body.to_dict()
        _kwargs['json'] = _body
        headers['Content-Type'] = 'application/json'
        _kwargs['headers'] = headers
        return _kwargs
    
    def _parse_response_getMessageReactions(self, response: httpx.Response) -> Optional[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
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
    
    def _build_response_getMessageReactions(self, response: httpx.Response) -> Response[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getMessageReactions(response=response))
    
    async def asyncio_detailed_getMessageReactions(self, id: int, body: GetMessageReactionsBody) -> Response[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
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
            Response[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]
        """
        kwargs = self._get_kwargs_getMessageReactions(id=id, body=body)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getMessageReactions(response=response)
    
    async def getMessageReactions(self, id: int, body: GetMessageReactionsBody) -> Optional[Union[BadRequest, GetMessageReactionsResponse200, NotFound]]:
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
        return (await self.asyncio_detailed_getMessageReactions(id=id, body=body)).parsed
    
    def _get_kwargs_deleteMessageReactions(self, id: str, code: str) -> dict[str, Any]:
        params: dict[str, Any] = {}
        params['code'] = code
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'delete', 'url': f'/messages/{id}/reactions', 'params': params}
        return _kwargs
    
    def _parse_response_deleteMessageReactions(self, response: httpx.Response) -> Optional[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
        if response.status_code == 204:
            response_204 = cast(Any, None)
            return response_204
        if response.status_code == 400:
            response_400 = DeleteMessageReactionsResponse400.from_dict(response.json())
            return response_400
        if response.status_code == 404:
            response_404 = DeleteMessageReactionsResponse404.from_dict(response.json())
            return response_404
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_deleteMessageReactions(self, response: httpx.Response) -> Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_deleteMessageReactions(response=response))
    
    async def asyncio_detailed_deleteMessageReactions(self, id: str, code: str) -> Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
        """Удаление реакции

         Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены
        авторизованным пользователем.

        Args:
            id (str):
            code (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]
        """
        kwargs = self._get_kwargs_deleteMessageReactions(id=id, code=code)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_deleteMessageReactions(response=response)
    
    async def deleteMessageReactions(self, id: str, code: str) -> Optional[Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]]:
        """Удаление реакции

         Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены
        авторизованным пользователем.

        Args:
            id (str):
            code (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, DeleteMessageReactionsResponse400, DeleteMessageReactionsResponse404]
        """
        return (await self.asyncio_detailed_deleteMessageReactions(id=id, code=code)).parsed
    
    def _get_kwargs_getEmployees(self, per: Union[Unset, int]=50, page: Union[Unset, int]=1, query: Union[Unset, str]=UNSET) -> dict[str, Any]:
        params: dict[str, Any] = {}
        params['per'] = per
        params['page'] = page
        params['query'] = query
        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        _kwargs: dict[str, Any] = {'method': 'get', 'url': '/users', 'params': params}
        return _kwargs
    
    def _parse_response_getEmployees(self, response: httpx.Response) -> Optional[GetEmployeesResponse200]:
        if response.status_code == 200:
            response_200 = GetEmployeesResponse200.from_dict(response.json())
            return response_200
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getEmployees(self, response: httpx.Response) -> Response[GetEmployeesResponse200]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getEmployees(response=response))
    
    async def asyncio_detailed_getEmployees(self, per: Union[Unset, int]=50, page: Union[Unset, int]=1, query: Union[Unset, str]=UNSET) -> Response[GetEmployeesResponse200]:
        """получение актуального списка всех сотрудников компании

         Fetch a paginated list of employees with optional filtering by query.

        Args:
            per (Union[Unset, int]):  Default: 50.
            page (Union[Unset, int]):  Default: 1.
            query (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[GetEmployeesResponse200]
        """
        kwargs = self._get_kwargs_getEmployees(per=per, page=page, query=query)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getEmployees(response=response)
    
    async def getEmployees(self, per: Union[Unset, int]=50, page: Union[Unset, int]=1, query: Union[Unset, str]=UNSET) -> Optional[GetEmployeesResponse200]:
        """получение актуального списка всех сотрудников компании

         Fetch a paginated list of employees with optional filtering by query.

        Args:
            per (Union[Unset, int]):  Default: 50.
            page (Union[Unset, int]):  Default: 1.
            query (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            GetEmployeesResponse200
        """
        return (await self.asyncio_detailed_getEmployees(per=per, page=page, query=query)).parsed
    
    def _get_kwargs_getEmployee(self, id: int) -> dict[str, Any]:
        _kwargs: dict[str, Any] = {'method': 'get', 'url': f'/users/{id}'}
        return _kwargs
    
    def _parse_response_getEmployee(self, response: httpx.Response) -> Optional[Union[GetEmployeeResponse200, NotFound]]:
        if response.status_code == 200:
            response_200 = GetEmployeeResponse200.from_dict(response.json())
            return response_200
        if response.status_code == 404:
            response_404 = NotFound.from_dict(response.json())
            return response_404
        if self.client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None
    
    def _build_response_getEmployee(self, response: httpx.Response) -> Response[Union[GetEmployeeResponse200, NotFound]]:
        return Response(status_code=HTTPStatus(response.status_code), content=response.content, headers=response.headers, parsed=self._parse_response_getEmployee(response=response))
    
    async def asyncio_detailed_getEmployee(self, id: int) -> Response[Union[GetEmployeeResponse200, NotFound]]:
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
        kwargs = self._get_kwargs_getEmployee(id=id)
        response = await self.client.get_async_httpx_client().request(**kwargs)
        return self._build_response_getEmployee(response=response)
    
    async def getEmployee(self, id: int) -> Optional[Union[GetEmployeeResponse200, NotFound]]:
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
        return (await self.asyncio_detailed_getEmployee(id=id)).parsed
    
    