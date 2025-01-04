# pachca = Pachca(
#     token='x4EhHyzYY2aA38GJb6AnKQXcY716LnEHCoxD1dUEyCI',
#     base_url = 'https://api.pachca.com/api/shared/v1'
# )
import asyncio

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models.query_chat import QueryChat

query_chat = QueryChat(name='tt')
chat_body = CreateChatBody(chat=query_chat)


pachca = Pachca(
    token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
)


async def main() -> None:
    """ Функция теста эндпоинтов """
    task1 = asyncio.create_task(pachca.createChat(body=chat_body))
    task2 = asyncio.create_task(pachca.getEmployees())
    task3 = asyncio.create_task(pachca.getTag(2736))

    print(await task1)
    print('*' * 30)
    print(await task2)
    print('*' * 30)
    print(await task3)


if __name__ == '__main__':
    asyncio.run(main())
