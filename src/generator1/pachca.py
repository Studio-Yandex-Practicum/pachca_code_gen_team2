# import asyncio

# from pachca_api_open_api_3_0_client.client import Pachca
# from pachca_api_open_api_3_0_client.models.create_chat_body import (
#     CreateChatBody,
# )
# from pachca_api_open_api_3_0_client.models.query_chat import QueryChat

# query_chat = QueryChat(name='test')
# chat_body = CreateChatBody(chat=query_chat)


# pachca = Pachca(
#     token='x4EhHyzYY2aA38GJb6AnKQXcY716LnEHCoxD1dUEyCI',
# )


# async def main() -> None:
#     """ Функция теста эндпоинтов """
#     task1 = asyncio.create_task(pachca.createChat(body=chat_body))
#     task2 = asyncio.create_task(pachca.getEmployees())

#     print(await task1)
#     print('*' * 30)
#     print(await task2)


# if __name__ == '__main__':
#     asyncio.run(main())

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

query_chat = QueryChat(name='test500')
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


pachca = Pachca(
    # token='x4EhHyzYY2aA38GJb6AnKQXcY716LnEHCoxD1dUEyCI',
    token='MnVVaQqJdjw5iRVcOoYJgZ440hTdUVArjl1idgx6iow',
)


async def main() -> None:
    """ Функция теста эндпоинтов """

    task1 = asyncio.create_task(pachca.createChat(body=chat_body))
    # task2 = asyncio.create_task(pachca.getEmployees())
    task3 = asyncio.create_task(pachca.postMembersToChats(
       id=999, body=members_body))
    # task4 = asyncio.create_task(pachca.postMembersToChats(
    #    id=17803544, body=members_body))
    task5 = asyncio.create_task(pachca.leaveChat(id=17837661))
    # task6 = asyncio.create_task(pachca.createMessage(body=message_body))

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
    # print(await task3)
    # print('*' * 30)
    # print(await task7)
    # print('*' * 30)
    # print(await task5)
    # print('*' * 30)
    print(await task5)


if __name__ == '__main__':
    asyncio.run(main())


# import asyncio

# from pachca_api_open_api_3_0_client.client import Pachca
# from pachca_api_open_api_3_0_client.models.create_chat_body import (
#     CreateChatBody,
# )
# from pachca_api_open_api_3_0_client.models.query_chat import QueryChat
# from pachca_api_open_api_3_0_client.models.edit_messages import EditMessages
# from pachca_api_open_api_3_0_client.models.create_message import (
#     CreateMessage)
# from pachca_api_open_api_3_0_client.models.create_message_body import (
#     CreateMessageBody)
# from pachca_api_open_api_3_0_client.models.edit_message_body import (
#     EditMessageBody)

# query_chat = QueryChat(name='Testing')

# chat_body = CreateChatBody(chat=query_chat)

# create_meassage = CreateMessage(
#     entity_id=1781540, content='NOT SUPER PUPER2222')

# edit_meassage = EditMessages(content='NOT and NOT SUPER PUPER')

# edit_message_body = EditMessageBody(message=edit_meassage)

# message_body = CreateMessageBody(message=create_meassage)

# pachca = Pachca(
#     token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
# )


# async def main() -> None:
#     """Функция теста эндпоинтов"""
#     task1 = asyncio.create_task(pachca.createMessage(body=message_body))
#     task2 = asyncio.create_task(pachca.getTag(2232323))
#     task3 = asyncio.create_task(pachca.deleteMessageReactions(
#         id=412338865, code='😭'))
#     task4 = asyncio.create_task(pachca.editMessage(
#         id=412502100, body=edit_message_body))
#     print(await task1)
#     print('*' * 30)
#     print(await task2)
#     print('*' * 30)
#     print(await task3)
#     print('*' * 30)
#     print(await task4)



# if __name__ == '__main__':
#     asyncio.run(main())


# Chat(id=17803822, name='test500', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 23, 42, 41, tzinfo=tzutc()), member_ids=[516675, 516682], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 23, 43, 51, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/test500-786bb7c6', additional_properties={})
# Chat(id=17803821, name='test4135435353534534534c5f4534d35f43d5453543d53543', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 23, 40, 52, tzinfo=tzutc()), member_ids=[516675], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 23, 40, 52, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/test4135435353534534534c5f4534d35f43d5453543d53543-12fb44cd', additional_properties={}),
# Chat(id=17803820, name='test413', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 23, 39, 33, tzinfo=tzutc()), member_ids=[516675], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 23, 39, 33, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/test413-c89b0dda', additional_properties={}),
# Chat(id=17803818, name='test313', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 23, 39, 13, tzinfo=tzutc()), member_ids=[516675, 516682], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 23, 39, 13, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/test313-9d324a08', additional_properties={}), 
# Chat(id=17803544, name='test3', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 20, 56, 27, tzinfo=tzutc()), member_ids=[516675, 516682], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 21, 32, 23, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/test3-1463d44f', additional_properties={}),
# Chat(id=17803212, name='', owner_id=516682, created_at=datetime.datetime(2025, 1, 5, 19, 21, 36, tzinfo=tzutc()), member_ids=[516675, 516682], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 19, 21, 36, 907000, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/chat-340f6b0f', additional_properties={}), 
# Chat(id=17802862, name='test', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 18, 16, 59, tzinfo=tzutc()), member_ids=[516675, 516682], group_tag_ids=[], channel=False, public=True, last_message_at=datetime.datetime(2025, 1, 6, 0, 10, 41, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/test-a65eb5e5', additional_properties={}),
# Chat(id=17802734, name='', owner_id=516675, created_at=datetime.datetime(2025, 1, 5, 17, 57, 22, tzinfo=tzutc()), member_ids=[516675], group_tag_ids=[], channel=False, public=False, last_message_at=datetime.datetime(2025, 1, 5, 17, 57, 22, 424000, tzinfo=tzutc()), meet_room_url='https://meet.pachca.com/chat-49dbdd83', additional_properties={})


# Chat(id=17837580,
# name='test500',
# owner_id=516675,
# created_at=datetime.datetime(2025, 1, 8, 16, 12, 6, tzinfo=tzutc()),
# member_ids=[516675],
# group_tag_ids=[],
# channel=False,
# public=False,
# last_message_at=datetime.datetime(2025, 1, 8, 16, 12, 6, tzinfo=tzutc()),
# meet_room_url='https://meet.pachca.com/test500-d14ec1c2',
# additional_properties={}),
# additional_properties={})