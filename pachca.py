import asyncio

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models.query_chat import QueryChat

query_chat = QueryChat(name='test')
chat_body = CreateChatBody(chat=query_chat)


pachca = Pachca(
    token='x4EhHyzYY2aA38GJb6AnKQXcY716LnEHCoxD1dUEyCI',
)


async def main():
    task2 = asyncio.create_task(pachca.createChat(body=chat_body))
    task3 = asyncio.create_task(pachca.getEmployees())

    print(await task2)
    print('*' * 30)
    print(await task3)


if __name__ == '__main__':
    asyncio.run(main())