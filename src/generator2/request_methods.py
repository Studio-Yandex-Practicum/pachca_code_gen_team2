from .models.models_reqBod_createChat import Createchat
from .models.models_reqBod_createMessage import Createmessage
from .models.models_reqBod_createTask import Createtask
from .models.models_reqBod_editMessage import Editmessage
from .models.models_reqBod_getDirectUrl import Getdirecturl
from .models.models_reqBod_postMembersToChats import Postmemberstochats
from .models.models_reqBod_postMessageReactions import Postmessagereactions
from .models.models_reqBod_postTagsToChats import Posttagstochats
from .models.models_reqBod_putStatus import Putstatus
from .models.models_response_createChatpost201 import ResponseCreatechatPost201
from .models.models_response_createChatpost422 import ResponseCreatechatPost422
from .models.models_response_createMessagepost201 import (
    ResponseCreatemessagePost201,
)
from .models.models_response_createMessagepost400 import (
    ResponseCreatemessagePost400,
)
from .models.models_response_createTaskpost201 import ResponseCreatetaskPost201
from .models.models_response_createTaskpost400 import ResponseCreatetaskPost400
from .models.models_response_createThreadpost200 import (
    ResponseCreatethreadPost200,
)
from .models.models_response_createThreadpost400 import (
    ResponseCreatethreadPost400,
)
from .models.models_response_deleteMessageReactionsdelete400 import (
    ResponseDeletemessagereactionsDelete400,
)
from .models.models_response_editMessageput200 import ResponseEditmessagePut200
from .models.models_response_editMessageput400 import ResponseEditmessagePut400
from .models.models_response_getChatget200 import ResponseGetchatGet200
from .models.models_response_getChatget400 import ResponseGetchatGet400
from .models.models_response_getChatsget200 import ResponseGetchatsGet200
from .models.models_response_getChatsget422 import ResponseGetchatsGet422
from .models.models_response_getCommonMethodsget200 import (
    ResponseGetcommonmethodsGet200,
)
from .models.models_response_getCommonMethodsget400 import (
    ResponseGetcommonmethodsGet400,
)
from .models.models_response_getEmployeeget200 import ResponseGetemployeeGet200
from .models.models_response_getEmployeeget400 import ResponseGetemployeeGet400
from .models.models_response_getEmployeesget200 import (
    ResponseGetemployeesGet200,
)
from .models.models_response_getListMessageget200 import (
    ResponseGetlistmessageGet200,
)
from .models.models_response_getListMessageget400 import (
    ResponseGetlistmessageGet400,
)
from .models.models_response_getMessageReactionsget200 import (
    ResponseGetmessagereactionsGet200,
)
from .models.models_response_getMessageReactionsget400 import (
    ResponseGetmessagereactionsGet400,
)
from .models.models_response_getMessageget200 import ResponseGetmessageGet200
from .models.models_response_getMessageget400 import ResponseGetmessageGet400
from .models.models_response_getStatusget200 import ResponseGetstatusGet200
from .models.models_response_getTagget200 import ResponseGettagGet200
from .models.models_response_getTagget400 import ResponseGettagGet400
from .models.models_response_getTagsEmployeesget200 import (
    ResponseGettagsemployeesGet200,
)
from .models.models_response_getTagsEmployeesget400 import (
    ResponseGettagsemployeesGet400,
)
from .models.models_response_getTagsget200 import ResponseGettagsGet200
from .models.models_response_getTagsget400 import ResponseGettagsGet400
from .models.models_response_getUploadspost200 import ResponseGetuploadsPost200
from .models.models_response_leaveChatdelete400 import (
    ResponseLeavechatDelete400,
)
from .models.models_response_postMembersToChatspost422 import (
    ResponsePostmemberstochatsPost422,
)
from .models.models_response_postMessageReactionspost400 import (
    ResponsePostmessagereactionsPost400,
)
from .models.models_response_postTagsToChatspost422 import (
    ResponsePosttagstochatsPost422,
)
from .models.models_response_putStatusput201 import ResponsePutstatusPut201
from .models.models_response_putStatusput400 import ResponsePutstatusPut400


async def get_common_methods(
    self, entity_type: str = None,
) -> ResponseGetcommonmethodsGet200:
    """получение списка актульных полей сущности

    Метод для получения актуального списка дополнительных полей участников и
    напоминаний в вашей компании. Тело запроса отсутствует, параметры передаются в
    URL (например, /custom_properties?entity_type=User)
    """
    client = await self.get_client()
    async with client:
        url = "/custom_properties"
        query_params = self.filter_query_params(entity_type=entity_type)
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGetcommonmethodsGet200.model_validate_json(
                response.text,
            )
        if response.is_client_error:
            return ResponseGetcommonmethodsGet400.model_validate_json(
                response.text,
            )
        return None


async def get_uploads(self) -> ResponseGetuploadsPost200:
    """получения подписи и ключа для загрузки файла

    Данный метод необходимо использовать для загрузки каждого файла.  Данный метод
    позволяет получить уникальный набор параметров для загрузки файла. Параметры
    запроса отсутствуют.
    """
    client = await self.get_client()
    async with client:
        url = "/uploads"
        response = await client.post(url)
        if response.is_success:
            return ResponseGetuploadsPost200.model_validate_json(response.text)
        return None


async def get_direct_url(self, data: Getdirecturl):
    """(полученный в ответе на запрос /uploads) загрузка файла

    Данный метод не требует авторизации.  Получив все параметры, вам необходимо
    сделать POST запрос в формате multipart/form-data на адрес, который был указан
    в поле direct_url, отправив полученные параметры и сам файл.
    """
    client = await self.get_client()
    async with client:
        url = "/direct_url"
        response = await client.post(url, json=data.model_dump())
        return


async def get_employees(
    self, per: int = None, page: int = None, query: str = None,
) -> ResponseGetemployeesGet200:
    """получение актуального списка всех сотрудников компании

    Метод для получения актуального списка сотрудников вашей компании. Тело запроса
    отсутствует, параметры передаются в URL (например,
    /users?per=50&page=2&query=example.com)
    """
    client = await self.get_client()
    async with client:
        url = "/users"
        query_params = self.filter_query_params(
            per=per, page=page, query=query,
        )
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGetemployeesGet200.model_validate_json(
                response.text,
            )
        return None


async def get_employee(self, id: int) -> ResponseGetemployeeGet200:
    """получение информации о сотруднике

    Метод для получения информации о сотруднике. Для получения сотрудника вам
    необходимо знать его id и указать его в URL запроса.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/users/{id}", {"id": id})
        response = await client.get(url)
        if response.is_success:
            return ResponseGetemployeeGet200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseGetemployeeGet400.model_validate_json(response.text)
        return None


async def get_status(self) -> ResponseGetstatusGet200:
    """получение информации о своем статусе

    Метод для получения информации о своем статусе. Параметры запроса отсутствуют.
    """
    client = await self.get_client()
    async with client:
        url = "/profile/status"
        response = await client.get(url)
        if response.is_success:
            return ResponseGetstatusGet200.model_validate_json(response.text)
        return None


async def put_status(self, data: Putstatus) -> ResponsePutstatusPut201:
    """новый статус

    Метод для установки себе нового статуса.
    """
    client = await self.get_client()
    async with client:
        url = "/profile/status"
        response = await client.put(url, json=data.model_dump())
        if response.is_success:
            return ResponsePutstatusPut201.model_validate_json(response.text)
        if response.is_client_error:
            return ResponsePutstatusPut400.model_validate_json(response.text)
        return None


async def del_status(self):
    """удаление своего статуса

    Метод для удаления своего статуса. Параметры запроса отсутствуют.
    """
    client = await self.get_client()
    async with client:
        url = "/profile/status"
        response = await client.delete(url)
        return


async def get_tag(self, id: int) -> ResponseGettagGet200:
    """получение информации о теге

    Метод для получения информации о теге. Названия тегов являются уникальными в
    компании.  Для получения тега вам необходимо знать его id и указать его в URL
    запроса. Параметры запроса отсутствуют
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/group_tags/{id}", {"id": id})
        response = await client.get(url)
        if response.is_success:
            return ResponseGettagGet200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseGettagGet400.model_validate_json(response.text)
        return None


async def get_tags(
    self, per: int = None, page: int = None,
) -> ResponseGettagsGet200:
    """получение актуального списка тегов сотрудников

    Метод для получения актуального списка тегов сотрудников.  Названия тегов
    являются уникальными в компании. Тело запроса отсутствует, параметры передаются
    в URL (например, /group_tags?per=10&page=2)
    """
    client = await self.get_client()
    async with client:
        url = "/group_tags"
        query_params = self.filter_query_params(per=per, page=page)
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGettagsGet200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseGettagsGet400.model_validate_json(response.text)
        return None


async def get_tags_employees(
    self, id: int, per: int = None, page: int = None,
) -> ResponseGettagsemployeesGet200:
    """получение актуального списка сотрудников тега

    Метод для получения актуального списка сотрудников тега.  Идентификатор тега,
    список сотрудников которого необходимо получить, и другие параметры передаются
    в URL (например, /group_tags/877650/users?per=3&page=2)
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/group_tags/{id}/users", {"id": id})
        query_params = self.filter_query_params(per=per, page=page)
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGettagsemployeesGet200.model_validate_json(
                response.text,
            )
        if response.is_client_error:
            return ResponseGettagsemployeesGet400.model_validate_json(
                response.text,
            )
        return None


async def get_chats(
    self,
    sort_field: str = "id",
    sort: str = "desc",
    per: int = None,
    page: int = None,
    availability: str = None,
    last_message_at_after: str = None,
    last_message_at_before: str = None,
) -> ResponseGetchatsGet200:
    """получение списка бесед и каналов

    Метод для получения списка бесед и каналов по заданным параметрам.  Тело
    запроса отсутствует, параметры передаются в URL (например,
    /chats?per=2&sort[id]=desc)
    """
    client = await self.get_client()
    async with client:
        url = "/chats"
        query_params = self.filter_query_params(
            sort_field=sort_field,
            sort=sort,
            per=per,
            page=page,
            availability=availability,
            last_message_at_after=last_message_at_after,
            last_message_at_before=last_message_at_before,
        )
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGetchatsGet200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseGetchatsGet422.model_validate_json(response.text)
        return None


async def create_chat(self, data: Createchat) -> ResponseCreatechatPost201:
    """создание новой беседы или канала

    Метод для создания новой беседы или нового канала. При создании беседы или
    канала вы автоматически становитесь участником.
    """
    client = await self.get_client()
    async with client:
        url = "/chats"
        response = await client.post(url, json=data.model_dump())
        if response.is_success:
            return ResponseCreatechatPost201.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseCreatechatPost422.model_validate_json(response.text)
        return None


async def get_chat(self, id: int) -> ResponseGetchatGet200:
    """получение информации о беседе или канале

    Получения информации о беседе или канале. Для получения беседы или канала вам
    необходимо знать её id и указать его в URL запроса.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/chats/{id}", {"id": id})
        response = await client.get(url)
        if response.is_success:
            return ResponseGetchatGet200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseGetchatGet400.model_validate_json(response.text)
        return None


async def post_members_to_chats(self, data: Postmemberstochats, id: int):
    """добавление пользователей в состав участников

    Метод для добавления пользователей в состав участников беседы или канала.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/chats/{id}/members", {"id": id})
        response = await client.post(url, json=data.model_dump())
        if response.is_client_error:
            return ResponsePostmemberstochatsPost422.model_validate_json(
                response.text,
            )
        return None


async def post_tags_to_chats(self, data: Posttagstochats, id: int):
    """добавление тегов в состав участников беседы или канала

    Метод для добавления тегов в состав участников беседы или канала.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/chats/{id}/group_tags", {"id": id})
        response = await client.post(url, json=data.model_dump())
        if response.is_client_error:
            return ResponsePosttagstochatsPost422.model_validate_json(
                response.text,
            )
        return None


async def leave_chat(self, id: int):
    """выход из беседы или канала

    Метод для самостоятельного выхода из беседы или канала. Параметры запроса
    отсутствуют/
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/chats/{id}/leave", {"id": id})
        response = await client.delete(url)
        if response.is_client_error:
            return ResponseLeavechatDelete400.model_validate_json(
                response.text,
            )
        return None


async def create_thread(self, id: int) -> ResponseCreatethreadPost200:
    """создание нового треда

    Метод для создания нового треда к сообщению. Если у сообщения уже был создан
    тред, то в ответе вернётся информация об уже созданном ранее треде.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/messages/{id}/thread", {"id": id})
        response = await client.post(url)
        if response.is_success:
            return ResponseCreatethreadPost200.model_validate_json(
                response.text,
            )
        if response.is_client_error:
            return ResponseCreatethreadPost400.model_validate_json(
                response.text,
            )
        return None


async def get_list_message(
    self, chat_id: int = None, per: int = None, page: int = None,
) -> ResponseGetlistmessageGet200:
    """получение списка сообщений чата

    Метод для получения списка сообщений бесед, каналов, тредов и личных сообщений.
    Для получения сообщений вам необходимо знать chat_id требуемой беседы, канала,
    треда или диалога, и указать его в URL запроса. Сообщения будут возвращены в
    порядке убывания даты отправки (то есть, сначала будут идти последние сообщения
    чата). Для получения более ранних сообщений чата доступны параметры per и page.
    Тело запроса отсутствует, параметры передаются в URL (например,
    /messages?chat_id=198&per=3)
    """
    client = await self.get_client()
    async with client:
        url = "/messages"
        query_params = self.filter_query_params(
            chat_id=chat_id, per=per, page=page,
        )
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGetlistmessageGet200.model_validate_json(
                response.text,
            )
        if response.is_client_error:
            return ResponseGetlistmessageGet400.model_validate_json(
                response.text,
            )
        return None


async def create_message(
    self, data: Createmessage,
) -> ResponseCreatemessagePost201:
    """создание нового сообщения

    Метод для отправки сообщения в беседу или канал, личного сообщения пользователю
    или комментария в тред.  При использовании entity_type: "discussion" (или
    просто без указания entity_type) допускается отправка любого chat_id в поле
    entity_id. То есть, сообщение можно отправить зная только идентификатор чата.
    При этом, вы имеете возможность отправить сообщение в тред по его
    идентификатору или личное сообщение по идентификатору пользователя.  Для
    отправки личного сообщения пользователю создавать чат не требуется.  Достаточно
    указать entity_type: "user" и идентификатор пользователя.  Чат будет создан
    автоматически, если между вами ещё не было переписки. Между двумя
    пользователями может быть только один личный чат.
    """
    client = await self.get_client()
    async with client:
        url = "/messages"
        response = await client.post(url, json=data.model_dump())
        if response.is_success:
            return ResponseCreatemessagePost201.model_validate_json(
                response.text,
            )
        if response.is_client_error:
            return ResponseCreatemessagePost400.model_validate_json(
                response.text,
            )
        return None


async def get_message(self, id: int) -> ResponseGetmessageGet200:
    """получение информации о сообщении

    Метод для получения информации о сообщении.  Для получения сообщения вам
    необходимо знать его id и указать его в URL запроса.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/messages/{id}", {"id": id})
        response = await client.get(url)
        if response.is_success:
            return ResponseGetmessageGet200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseGetmessageGet400.model_validate_json(response.text)
        return None


async def edit_message(
    self, data: Editmessage, id: int,
) -> ResponseEditmessagePut200:
    """редактирование сообщения по указанному идентификатору

    Метод для редактирования сообщения или комментария.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/messages/{id}", {"id": id})
        response = await client.put(url, json=data.model_dump())
        if response.is_success:
            return ResponseEditmessagePut200.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseEditmessagePut400.model_validate_json(response.text)
        return None


async def get_message_reactions(
    self, id: int, per: int = None, page: int = None,
) -> ResponseGetmessagereactionsGet200:
    """получение актуального списка реакций

    Метод для получения актуального списка реакций на сообщение.  Идентификатор
    сообщения, список реакций на которое необходимо получить, передается в URL
    (например, /messages/7231942/reactions). Количество возвращаемых сущностей и
    страница выборки указываются в теле запроса
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/messages/{id}/reactions", {"id": id})
        query_params = self.filter_query_params(per=per, page=page)
        response = await client.get(url, params=query_params)
        if response.is_success:
            return ResponseGetmessagereactionsGet200.model_validate_json(
                response.text,
            )
        if response.is_client_error:
            return ResponseGetmessagereactionsGet400.model_validate_json(
                response.text,
            )
        return None


async def post_message_reactions(self, data: Postmessagereactions, id: int):
    """добавление реакции

    Метод для добавления реакции на сообщение. **Лимиты реакций:** - Каждый
    пользователь может установить не более 20 уникальных реакций на сообщение. -
    Сообщение может иметь не более 30 уникальных реакций. - Сообщение может иметь
    не более 1000 реакций.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/messages/{id}/reactions", {"id": id})
        response = await client.post(url, json=data.model_dump())
        if response.is_client_error:
            return ResponsePostmessagereactionsPost400.model_validate_json(
                response.text,
            )
        return None


async def delete_message_reactions(self, id: int, code: str = None):
    """удаление реакции

    Метод для удаления реакции на сообщение.  Удалить можно только те реакции,
    которые были поставлены авторизованным пользователем.
    """
    client = await self.get_client()
    async with client:
        url = self.format_url("/messages/{id}/reactions", {"id": id})
        query_params = self.filter_query_params(code=code)
        response = await client.delete(url, params=query_params)
        if response.is_client_error:
            return ResponseDeletemessagereactionsDelete400.model_validate_json(
                response.text,
            )
        return None


async def create_task(self, data: Createtask) -> ResponseCreatetaskPost201:
    """создание нового напоминания

    Метод для создания нового напоминания.  При создании напоминания обязательным
    условием является указания типа напоминания: звонок, встреча, простое
    напоминание, событие или письмо.  При этом не требуется дополнительное описание
    - вы просто создадите напоминание с соответствующим текстом. Если вы укажите
    описание напоминания - то именно оно и станет текстом напоминания. У
    напоминания должны быть ответственные, если их не указывать - ответственным
    назначаетесь вы.
    """
    client = await self.get_client()
    async with client:
        url = "/tasks"
        response = await client.post(url, json=data.model_dump())
        if response.is_success:
            return ResponseCreatetaskPost201.model_validate_json(response.text)
        if response.is_client_error:
            return ResponseCreatetaskPost400.model_validate_json(response.text)
        return None
