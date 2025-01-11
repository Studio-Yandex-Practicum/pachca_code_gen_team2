# import asyncio

# from pachca_api_open_api_3_0_client.client import Pachca
# from pachca_api_open_api_3_0_client.models.chat import Chat
# from pachca_api_open_api_3_0_client.models.create_chat_body import (
#     CreateChatBody,
# )
# from pachca_api_open_api_3_0_client.models import Message
# from pachca_api_open_api_3_0_client.models.create_message_body import (
#     CreateMessageBody,
# )

# create_message = Message(
#         entity_id=17945380, content='Super puper')
# query_chat = Chat(name='test')
# chat_body = CreateChatBody(chat=query_chat)
# message_body = CreateMessageBody(message=create_message)

# pachca = Pachca(
#     token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
# )


# async def main() -> None:
#     """Функция теста эндпоинтов"""
#     task1 = asyncio.create_task(pachca.createThread(id=414142273))
#     task2 = asyncio.create_task(pachca.getEmployee(123))
#     task3 = asyncio.create_task(
#         pachca.createMessage(body=message_body))
#     task4 = asyncio.create_task(pachca.leaveChat(id=111))
#     task5 = asyncio.create_task(pachca.deleteMessageReactions(
#         id=123, code='😭'))


#     print(await task1)
#     print('*' * 30)
#     print(await task2)
#     print('*' * 30)
#     print(await task3)
#     print('*' * 30)
#     print(await task4)
#     print('*' * 30)
#     print(await task5)

# id=17945380
# if __name__ == '__main__':
#     asyncio.run(main())


import asyncio
import datetime
import os

from dotenv import load_dotenv
from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models.create_message_body import (
    CreateMessageBody,
)
from pachca_api_open_api_3_0_client.models.create_messages import (
    CreateMessages,
)
from pachca_api_open_api_3_0_client.models.create_task_body import (
    CreateTaskBody,
)

from pachca_api_open_api_3_0_client.models import (
    CreateTaskBodyTask, QueryStatusStatus
)


'''
from pachca_api_open_api_3_0_client.models.edit_messages import EditMessages
from pachca_api_open_api_3_0_client.models.edit_message_body import (
    EditMessageBody
)
'''
from pachca_api_open_api_3_0_client.models.base_chat import BaseChat
from pachca_api_open_api_3_0_client.models.code_reaction import (
    CodeReaction,
)

# from pachca_api_open_api_3_0_client.models.get_message_reactions_body import (
#     GetMessageReactionsBody,
# )
from pachca_api_open_api_3_0_client.models.put_status_body import (
    PutStatusBody,
)

load_dotenv()
pachca = Pachca(os.getenv('TOKEN'))


async def main() -> None:
    """ Функция теста эндпоинтов """

    # подготовка запроса на создание беседы -->
    query_chat = BaseChat(name='test500_2')
    chat_body = CreateChatBody(chat=query_chat)
    # <--
    # запрос на создание беседы
    chat_create = asyncio.create_task(
        pachca.createChat(body=chat_body))
    chat_response = await chat_create
    print(chat_response)
    print('*' * 60)

    # запрос на получение списка бесед и каналов
    print(await asyncio.create_task(pachca.getChats()))
    print('*' * 60)

    # запрос на получение информации о беседе
    print(await asyncio.create_task(
        pachca.getChat(id=chat_response.data.id))
    )
    print('*' * 60)

    # подготовка запроса на создание сообщения в созданную беседу -->
    create_message = CreateMessages(
        entity_id=chat_response.data.id, content='Super puper')
    message_body = CreateMessageBody(message=create_message)
    # <--
    # запрос на создание сообщения в созданную беседу
    message_create = asyncio.create_task(
        pachca.createMessage(body=message_body))
    message_response = await message_create
    print(message_response)
    print('*' * 60)

    # создание треда к созданному сообщению
    thread_create = asyncio.create_task(
        pachca.createThread(id=message_response.data.id)
    )
    print(await thread_create)
    print('*' * 60)

    # запрос на получение списка сообщений
    print(await asyncio.create_task(
        pachca.getListMessage(chat_id=chat_response.data.id))
    )
    print('*' * 60)

    # запрос на получение сообщения
    print(await asyncio.create_task(
        pachca.getMessage(id=message_response.data.id))
    )
    print('*' * 60)
    '''
    Запрос проходит успешно, но в yaml схема ответа прописана не корректно.
    Поэтому успешный ответ приводит AttributeError.
    # подготовка запроса на редактирование сообщения -->
    edit_meassage = EditMessages(content='NOT SUPER PUPER')
    edit_message_body = EditMessageBody(message=edit_meassage)
    # <--
    # запрос на редактирование сообщения
    print(await asyncio.create_task(
        pachca.editMessage(
            id=message_response.data.id, body=edit_message_body)
        )
    )
    print('*' * 60)
    '''

    # подготовка запроса на добавление реакции к сообщению -->
    post_reactions = CodeReaction(code='😭')
    # <--
    # запрос на добавление реакции к сообщению
    print(await asyncio.create_task(
        pachca.postMessageReactions(
            id=message_response.data.id, body=post_reactions)
        )
    )
    print('*' * 60)

    # подготовка запроса на получение списка реакций к сообщению -->
    # <--
    # запрос на получение списка реакций
    print(await asyncio.create_task(
        pachca.getMessageReactions(id=message_response.data.id))
    )
    print('*' * 60)

    # запрос на удаление реакции
    print(await asyncio.create_task(
        pachca.deleteMessageReactions(id=message_response.data.id, code='😭')
        )
    )
    print('*' * 60)

    # подготовка запроса на создание напоминания -->
    create_body_task = CreateTaskBodyTask(
        kind='call',
        content='Звонок другу',
        due_at=datetime.datetime.now(),
    )
    body_task = CreateTaskBody(task=create_body_task)
    # <--
    # запрос на создание напоминания
    print(await asyncio.create_task(pachca.createTask(body=body_task)))
    print('*' * 60)

    # запрос на получения списка пользователей
    users_response = await asyncio.create_task(pachca.getEmployees())
    print(users_response)
    print('*' * 60)

    # запрос на получение информации о пользователе
    print(await asyncio.create_task(
        pachca.getEmployee(id=users_response.data[0].id))
    )
    print('*' * 60)

    # подготовка запроса на добавление статуса -->
    query_status = QueryStatusStatus(
        emoji='😭',
        title='Я не плачу это просто слезы',
        expires_at=None
    )
    # <--
    # запрос на добавление статуса
    print(await asyncio.create_task(pachca.putStatus(body=query_status)))
    print('*' * 60)

    # запрос на получение информации о своем статусе
    print(await asyncio.create_task(pachca.getStatus()))
    print('*' * 60)

    '''
    В client.py отсутствует метод delStatus
    # запрос на удаление статуса
    print(await asyncio.create_task(pachca.delStatus()))
    print('*' * 60)
    '''

    # запрос на получение тегов сотрудников
    print(await asyncio.create_task(pachca.getTags()))
    print('*' * 60)

    # запрос на получение списка актуальных полей сущности
    print(await asyncio.create_task(
        pachca.getCommonMethods(entity_type='User'))
    )
    print('*' * 60)

    # запрос получения подписи и ключа для загрузки файла
    print(await asyncio.create_task(pachca.getUploads()))
    print('*' * 60)

if __name__ == '__main__':
    asyncio.run(main())
