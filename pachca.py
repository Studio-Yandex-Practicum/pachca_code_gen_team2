import asyncio

from pachca_api_open_api_3_0_client import AuthenticatedClient
from pachca_api_open_api_3_0_client.api.chats_and_channels.create_chat import (
    asyncio as as2,
)
from pachca_api_open_api_3_0_client.api.employees.get_employees import (
    asyncio as as1,
)
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


async def main():
    task1 = asyncio.create_task(as1(client=client))
    task2 = asyncio.create_task(as2(client=client, body=chat_body))

    print(await task1)
    print('*' * 30)
    print(await task2)


if __name__ == '__main__':
    asyncio.run(main())
