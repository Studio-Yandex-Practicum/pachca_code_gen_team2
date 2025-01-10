import asyncio

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.chat import Chat
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)

query_chat = Chat(name='test')
chat_body = CreateChatBody(chat=query_chat)


pachca = Pachca(
    token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
)


async def main() -> None:
    """Функция теста эндпоинтов"""
    task1 = asyncio.create_task(pachca.createChat(body=chat_body))
    task2 = asyncio.create_task(pachca.getEmployee(123))

    print(await task1)
    print('*' * 30)
    print(await task2)


if __name__ == '__main__':
    asyncio.run(main())