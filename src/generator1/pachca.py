import asyncio
import datetime
import os

from dotenv import load_dotenv

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.chat import Chat
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
    CreateTaskBodyTask, QueryStatusStatus, EditMessages, EditMessageBody
)

from pachca_api_open_api_3_0_client.models.base_chat import BaseChat
from pachca_api_open_api_3_0_client.models.code_reaction import (
    CodeReaction,
)

from pachca_api_open_api_3_0_client.models.put_status_body import (
    PutStatusBody,
)

from logger_setup import setup_logging


load_dotenv()
pachca = Pachca(os.getenv('TOKEN'))

logger = setup_logging('test_requests_logging')


async def main() -> None:
    """ Функция теста эндпоинтов """

    query_chat = BaseChat(name='test500_2')
    chat_body = CreateChatBody(chat=query_chat)

    chat_create = asyncio.create_task(
        pachca.createChat(body=chat_body))

    chat_response = await chat_create

    # запрос на получение списка бесед и каналов

    create_task = await asyncio.create_task(pachca.getChats())

    # запрос на получение информации о беседе

    getChat = await asyncio.create_task(
        pachca.getChat(id=chat_response.data.id)
    )

    # подготовка запроса на создание сообщения в созданную беседу -->

    create_message = CreateMessages(

        entity_id=chat_response.data.id, content='Super puper')

    message_body = CreateMessageBody(message=create_message)

    # запрос на создание сообщения в созданную беседу

    message_create = asyncio.create_task(
        pachca.createMessage(body=message_body))

    message_response = await message_create

    # создание треда к созданному сообщению

    thread_create = asyncio.create_task(
        pachca.createThread(id=message_response.data.id)
    )

    # запрос на получение списка сообщений

    getListMessage = await asyncio.create_task(

        pachca.getListMessage(chat_id=chat_response.data.id))

    # запрос на получение сообщения

    getMessage = await asyncio.create_task(

        pachca.getMessage(id=message_response.data.id))

    # подготовка запроса на редактирование сообщения -->

    edit_meassage = EditMessages(content='NOT SUPER PUPER')

    edit_message_body = EditMessageBody(message=edit_meassage)

    # запрос на редактирование сообщения

    editMessage = await asyncio.create_task(
        pachca.editMessage(
            id=message_response.data.id, body=edit_message_body)
        )

    # запрос на удаление статуса

    print(await asyncio.create_task(pachca.delStatus()))

    # запрос на получение тегов сотрудников

    print(await asyncio.create_task(pachca.getTags()))

    # запрос на получение списка актуальных полей сущности

    print(await asyncio.create_task(

        pachca.getCommonMethods(entity_type='User'))

    )
    post_reactions = CodeReaction(code='😭')
    postMessageReactions = await pachca.postMessageReactions(
        id=message_response.data.id, body=post_reactions
    )

    getMessageReactions = await pachca.getMessageReactions(id=message_response.data.id)

    deleteMessageReactions = await pachca.deleteMessageReactions(id=message_response.data.id, code='😭')

    # запрос на создание напоминания

    create_body_task = CreateTaskBodyTask(
        kind='call',
        content='Звонок другу',
        due_at=datetime.datetime.now(),
    )

    body_task = CreateTaskBody(task=create_body_task)
    # <--
    
    createtaskbody = await asyncio.create_task(pachca.createTask(body=body_task))

    users_response = await asyncio.create_task(pachca.getEmployees())

    getEmployee = await asyncio.create_task(pachca.getEmployee(id=users_response.data[0].id))

    # запрос получения подписи и ключа для загрузки файла

    logger.debug(await pachca.getUploads())

    for task in (
        chat_response,
        create_task,
        getChat,
        message_response,
        thread_create,
        getListMessage,
        getMessage,
        editMessage,
        create_task,
        postMessageReactions,
        getMessageReactions,
        deleteMessageReactions,
        createtaskbody,
        users_response,
        getEmployee
    ):

        result = task

        logger.debug(
            f"{task}: data={result} \n"
            "**"
        )

if __name__ == '__main__':
    asyncio.run(main())
