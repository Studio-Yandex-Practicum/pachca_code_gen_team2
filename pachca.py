import asyncio

from pachca_api_open_api_3_0_client.api.chats_and_channels.create_chat import (
    createChat,
)
from pachca_api_open_api_3_0_client.api.employees.get_employees import (
    getEmployees,
)
from pachca_api_open_api_3_0_client.client import AuthenticatedClient, Pachca
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models.query_chat import QueryChat

client = AuthenticatedClient(
    base_url='https://api.pachca.com/api/shared/v1',
    token='35KekGygDNiFwtPpqUe44CaEZ_EVL17ycYRJrMnvHOs',
)

query_chat = QueryChat(name='test')
chat_body = CreateChatBody(chat=query_chat)


pachca = Pachca(
    base_url='https://api.pachca.com/api/shared/v1',
    token='35KekGygDNiFwtPpqUe44CaEZ_EVL17ycYRJrMnvHOs',
)


async def main():
    task2 = asyncio.create_task(pachca.createChat(body=chat_body))
    task3 = asyncio.create_task(pachca.getEmployees())

    print('*' * 30)
    print(await task2)
    print('*' * 30)
    print(await task3)


if __name__ == '__main__':
    asyncio.run(main())
