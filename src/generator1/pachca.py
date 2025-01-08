import asyncio
import datetime

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models.create_message import (
    CreateMessage)
from pachca_api_open_api_3_0_client.models.create_message_body import (
    CreateMessageBody)
from pachca_api_open_api_3_0_client.models.create_task_body import (
    CreateTaskBody)
from pachca_api_open_api_3_0_client.models.create_task_body_task import (
    CreateTaskBodyTask)
from pachca_api_open_api_3_0_client.models.edit_message_body import (
    EditMessageBody)
from pachca_api_open_api_3_0_client.models.edit_messages import EditMessages
from pachca_api_open_api_3_0_client.models.get_message_reactions_body import (
    GetMessageReactionsBody)
from pachca_api_open_api_3_0_client.models.post_message_reactions_body import (
    PostMessageReactionsBody)
from pachca_api_open_api_3_0_client.models.query_chat import QueryChat
from pachca_api_open_api_3_0_client.models.post_members_to_chats_body import (
    PostMembersToChatsBody,
)

query_chat = QueryChat(name='Testing')

chat_body = CreateChatBody(chat=query_chat)
members_body = PostMembersToChatsBody(member_ids=[516675])
members_body = PostMembersToChatsBody(member_ids=[516682])
create_meassage = CreateMessage(
    entity_id=17802862, content='NOT SUPER PUPER2222')
# edit_meassage = EditMessages(content='NOT and NOT SUPER PUPER')
edit_meassage = EditMessages(content='Вот так  вот!')
message_body = CreateMessageBody(message=create_meassage)
edit_message_body = EditMessageBody(message=edit_meassage)
post_reactions = PostMessageReactionsBody(code='😭')
reaction_body = GetMessageReactionsBody()
create_body_task = CreateTaskBodyTask(
    kind='call',
    content='Звонок другу',
    due_at=datetime.datetime.now(),
)
body_task = CreateTaskBody(task=create_body_task)

create_meassage = CreateMessage(
    entity_id=1781540, content='NOT SUPER PUPER2222')

edit_meassage = EditMessages(content='NOT and NOT SUPER PUPER')

edit_message_body = EditMessageBody(message=edit_meassage)

message_body = CreateMessageBody(message=create_meassage)

pachca = Pachca(
    # token='x4EhHyzYY2aA38GJb6AnKQXcY716LnEHCoxD1dUEyCI',
    token='MnVVaQqJdjw5iRVcOoYJgZ440hTdUVArjl1idgx6iow',
    # token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
)


async def main() -> None:
    """ Функция теста эндпоинтов """

    task6 = asyncio.create_task(pachca.postMembersToChats(
       id=999, body=members_body))
    task5 = asyncio.create_task(pachca.leaveChat(id=111))
    task7 = asyncio.create_task(pachca.createThread(id=412338865))
    # task8 = asyncio.create_task(pachca.getListMessage(chat_id=17802862))
    # task9 = asyncio.create_task(pachca.getMessage(id=412338865))
    # task10 = asyncio.create_task(pachca.editMessage(
    #    id=412338865, body=edit_message_body)
    # )
    # task11 = asyncio.create_task(pachca.postMessageReactions(
    #    id=412338865, body=post_reactions)
    # )
    # task12 = asyncio.create_task(pachca.deleteMessageReactions(
    #    id=412338865, code='😭')
    # )
    # task13 = asyncio.create_task(pachca.getMessageReactions(
    #    id=412338865, body=reaction_body)
    # )
    # task14 = asyncio.create_task(pachca.createTask(body=body_task))
    """Функция теста эндпоинтов"""
    task1 = asyncio.create_task(pachca.createMessage(body=message_body))
    task2 = asyncio.create_task(pachca.getTag(2232323))
    task3 = asyncio.create_task(pachca.deleteMessageReactions(
        id=412338865, code='😭'))
    task4 = asyncio.create_task(pachca.editMessage(
        id=412502100, body=edit_message_body))
    print(await task1)
    print('*' * 30)
    print(await task2)
    print('*' * 30)
    print(await task3)
    print('*' * 30)
    print(await task4)
    print('*' * 30)
    print(await task5)
    print('*' * 30)
    print(await task6)
    print('*' * 30)
    print(await task7)
    # print('*' * 30)

if __name__ == '__main__':
    asyncio.run(main())