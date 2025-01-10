import asyncio

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.chat import Chat
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models import Message
from pachca_api_open_api_3_0_client.models.create_message_body import (
    CreateMessageBody,
)

create_message = Message(
        entity_id=17945380, content='Super puper')
query_chat = Chat(name='test')
chat_body = CreateChatBody(chat=query_chat)
message_body = CreateMessageBody(message=create_message)

pachca = Pachca(
    token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
)


async def main() -> None:
    """Функция теста эндпоинтов"""
    task1 = asyncio.create_task(pachca.createThread(id=414142273))
    task2 = asyncio.create_task(pachca.getEmployee(123))
    task3 = asyncio.create_task(
        pachca.createMessage(body=message_body))
    task4 = asyncio.create_task(pachca.leaveChat(id=111))
    task5 = asyncio.create_task(pachca.deleteMessageReactions(
        id=123, code='😭'))


    print(await task1)
    print('*' * 30)
    print(await task2)
    print('*' * 30)
    print(await task3)
    print('*' * 30)
    print(await task4)
    print('*' * 30)
    print(await task5)

id=17945380
if __name__ == '__main__':
    asyncio.run(main())
