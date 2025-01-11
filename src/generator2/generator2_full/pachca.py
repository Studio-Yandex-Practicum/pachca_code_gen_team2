import asyncio
import os

from dotenv import load_dotenv

from .bot import Bot
from .models.models_reqBod_putStatus import Putstatus
from .models.models_reqBod_createChat import Createchat
from .models.models_reqBod_createTask import Createtask
from .models.models_reqBod_postMessageReactions import Postmessagereactions
from .models.models_reqBod_editMessage import Editmessage
from .models.models_reqBod_postTagsToChats import Posttagstochats
from .models.models_reqBod_createMessage import Createmessage, Message
from .models.models_reqBod_postMembersToChats import Postmemberstochats

load_dotenv()

if __name__ == '__main__':

    print(id(Bot))
    print(Bot)
    pachca = Bot(token=f'Bearer {os.environ.get("TOKEN", "LOOKUP FAILED!")}')

    print(pachca.token)
    print(hasattr(pachca, 'get_common_methods'))

    message_test = Createmessage(message=Message(
        entity_type="discussion",
        entity_id=17579010,
        content="Вчера мы продали 756 футболок (что на 10% больше, чем в прошлое воскресенье)",
    ))
    #print(message_test.model_dump())
    async def run_pachca():
        print(await pachca.get_employee(id=515190))
        print(await pachca.get_employees())
        print(await pachca.get_chats(per=2))
        message = await pachca.create_message(data=message_test)
        print(message)
        print(await pachca.get_common_methods()) #Возвращает ошибку, нужно прописать обработку если (parameters.query и parameters.required)

        # # Создание беседы.
        # created_chat = await pachca.create_chat(
        #     data=Createchat(
        #         chat={
        #             'name': 'Тестовая беседа 31',
        #             'channel': False,
        #             'public': True
        #         }
        #     )
        # )
        # print('create_chat', created_chat, '\n','*'*60)

        # # Получение всех бесед данного рабочего пространства (РП токена)
        # all_chats = await pachca.get_chats()
        # print('get_chats', all_chats, '\n','*'*60)

        # # Получение конкретной беседы по id
        # chat = await pachca.get_chat(created_chat.data.id)
        # print('get_chat', chat, '\n','*'*60)

        # # Подключение пользователей к беседе.
        # response_post_members = await pachca.post_members_to_chats(
        #     id=chat.data.id,
        #     data=Postmemberstochats(
        #         member_ids=[515190],
        #         silent=False
        #     )
        # )
        # print('post_members_to_chats', response_post_members, '\n','*'*60)

        # # Создание нового сообщения в беседе.
        # response_create_message = await pachca.create_message(
        #     data=Createmessage(
        #         message={
        #             'content': f'Запощеное сообщение в беседу {chat.data.id}',
        #             'entity_type': 'discussion',
        #             'entity_id': chat.data.id
        #         }
        #     )
        # )
        # print('create_message', response_create_message, '\n','*'*60)

        # # Добавление тегов чату, пока неот способа создавать теги.
        # # response = await pachca.post_tags_to_chats(
        # #     id=17519775,
        # #     data=Posttagstochats(
        # #         group_tag_ids=[1, 2, 3]
        # #     )
        # # )

        # # Получение списка тегов
        # print(await pachca.get_tags())

        # # Получение всех сотрудников с тегом с id.
        # # print(await pachca.get_tags_employees()

        # # Создание треда к конкретному сообщению с id.
        # response_create_thread = await pachca.create_thread(
        #     id=response_create_message.data.id
        # )
        # print('create_thread', response_create_thread, '\n','*'*60)

        # # Создание комментария в треде другого сообщения
        # response_create_message_in_thread = await pachca.create_message(
        #     data=Createmessage(
        #         message={
        #             'content': f'Новое сообщение в тред {response_create_thread.data.id}',
        #             'entity_type': 'thread',
        #             'entity_id': response_create_thread.data.id
        #         }
        #     )
        # )
        # print('create_message_in_thread', response_create_message_in_thread, '\n','*'*60)

        # # Получение списка всех сообщений конкретного треда или беседы с пагинацией
        # response_list_messages = await pachca.get_list_message(
        #     chat_id=response_create_thread.data.chat_id, per=10, page=1
        # )
        # print('get_list_message', response_list_messages, '\n','*'*60)

        # # Получение конкретного сообщения по id
        # response_get_message = await pachca.get_message(
        #     id=response_create_message_in_thread.data.id
        # )
        # print('get_message', response_get_message, '\n','*'*60)

        # # Редактирование конкретного сообщения по его id
        # response_edit_message = await pachca.edit_message(
        #     id=response_create_message_in_thread.data.id,
        #     data=Editmessage(message={
        #         'content': ('РЕДАКТИРОВАНИЕ СООБЩЕНИЯ '
        #                     f'{response_create_message_in_thread.data.id} '
        #                     'ЧЕРЕЗ АПИ СОВЕРШЕНО УСПЕШНО')
        #     })
        # )
        # print('edit_message', response_edit_message, '\n','*'*60)

        # # Добавление реакции к сообщению с id
        # response_add_reaction = await pachca.post_message_reactions(
        #     id=response_edit_message.data.id,
        #     data=Postmessagereactions(code='👍')
        # )
        # response_add_reaction = await pachca.post_message_reactions(
        #     id=response_edit_message.data.id,
        #     data=Postmessagereactions(code='😱')
        # )
        # print('post_message_reactions', response_add_reaction, '\n','*'*60)

        # # Получение списка всех реакций конкретного сообщения.
        # response_message_reactions = await pachca.get_message_reactions(
        #     id=response_edit_message.data.id,
        # )
        # print('get_message_reactions', response_message_reactions, '\n','*'*60)

        # # Удаение конкретной реакции у конкретного сообщения.
        # response_delete_reaction = await pachca.delete_message_reactions(
        #     id=response_edit_message.data.id,
        #     code='😱'
        # )
        # print('delete_message_reactions', response_delete_reaction, '\n','*'*60)

        # # Создание напоминания
        # response_create_task = await pachca.create_task(
        #     data=Createtask(
        #         task={
        #             'kind': 'reminder',
        #             'content': 'дата в прошлом',
        #             'priority': 3,
        #             'due_at': '2025-12-24T18:00:29.000Z'
        #         }
        #     )
        # )
        # print('create_task', response_create_task, '\n','*'*60)

        # # Метод для того чтобы покинуть конкретный чат (беседу)
        # response = await pachca.leave_chat(
        #     id=created_chat.data.id
        # )
        # print(response)

        # Получить список всех сотрудников рабочего пространства.
        response_get_users = await pachca.get_employees()
        print('get_employees', response_get_users, '\n','*'*60)
        print(response_get_users.data[0].id)

        # Получить конкретного сотрудника рабочего простанства.
        response_get_user = await pachca.get_employee(
            response_get_users.data[0].id
        )
        print('get_employee', response_get_user, '\n','*'*60)

        # Добавить статус текущему пользователю, обладателю токена.
        response_put_status = await pachca.put_status(
            data=Putstatus(
                status={
                    'emoji': '😱',
                    'expires_at': '2025-12-24T17:47:25.000Z',
                    'title': 'Статус из клиента АПИ'
                }
            )
        )
        print('put_status', response_put_status, '\n','*'*60)

        # Получить статус текущего пользователя, обладателя токена.
        response_get_status = await pachca.get_status()
        print('get_status', response_get_status, '\n','*'*60)

        # Удалить статус текущему пользователю, обладателю токена.
        response_del_status = await pachca.del_status()
        print('del_status', response_del_status, '\n','*'*60)


    asyncio.run(run_pachca())

    # print(type(pachca))
    # print(pachca.__class__)
    # print(pachca.__class__.__class__)
    # print(pachca.__class__.__class__.__class__)