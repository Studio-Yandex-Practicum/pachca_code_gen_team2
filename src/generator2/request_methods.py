"""Сгенерированные методы запроса."""



async def get_common_methods(self, entity_type: str = None):
    """Список дополнительных полей

Метод для получения актуального списка дополнительных полей участников и
напоминаний в вашей компании."""
    client = await self.get_client()
    async with client:
        url = '/custom_properties'
        response = await client.get(url, params={ 'entity_type': entity_type })
        response.raise_for_status()
    return response.json()


async def get_uploads(self):
    """Получение подписи и ключа для загрузки файла

Возвращает параметры, необходимые для безопасной загрузки файла."""
    client = await self.get_client()
    async with client:
        url = '/uploads'
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def get_direct_url(self):
    """Получение URL для загрузки

Отправляет запрос для получения URL для безопасной загрузки файла."""
    client = await self.get_client()
    async with client:
        url = '/direct_url'
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def get_employees(self, per: int = None, page: int = None, query: str = None):
    """получение актуального списка всех сотрудников компании

Fetch a paginated list of employees with optional filtering by query."""
    client = await self.get_client()
    async with client:
        url = '/users'
        response = await client.get(url, params={ 'per': per, 'page': page, 'query': query })
        response.raise_for_status()
    return response.json()


async def get_employee(self, id: int):
    """получение информации о сотруднике

Метод для получения информации о сотруднике. Для получения сотрудника вам
необходимо знать его id и указать его в URL запроса."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/users/{id}', {'id': id})
        response = await client.get(url)
        response.raise_for_status()
    return response.json()


async def del_status(self):
    """удаление своего статуса

Параметры запроса отсутствуют"""
    client = await self.get_client()
    async with client:
        url = '/profile/status'
        response = await client.delete(url)
        response.raise_for_status()
    return response.json()


async def get_tag(self, id: int):
    """Информация о теге

Параметры запроса отсутствуют"""
    client = await self.get_client()
    async with client:
        url = self.format_url('/group_tags/{id}', {'id': id})
        response = await client.get(url)
        response.raise_for_status()
    return response.json()


async def get_tags(self, per: int = None, page: int = None):
    """Список тегов сотрудников

Метод для получения актуального списка тегов сотрудников."""
    client = await self.get_client()
    async with client:
        url = '/group_tags'
        response = await client.get(url, params={ 'per': per, 'page': page })
        response.raise_for_status()
    return response.json()


async def get_tags_employees(self, id: int, per: int = None, page: int = None):
    """получение актуального списка сотрудников тега

Метод для получения актуального списка сотрудников тега."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/group_tags/{id}/users', {'id': id})
        response = await client.get(url, params={ 'per': per, 'page': page })
        response.raise_for_status()
    return response.json()


async def create_chat(self):
    """Новая беседа или канал

Метод для создания новой беседы или нового канала. При создании беседы или
канала вы автоматически становитесь участником."""
    client = await self.get_client()
    async with client:
        url = '/chats'
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def get_chat(self, id: int):
    """Информация о беседе или канале

Получения информации о беседе или канале. Для получения беседы или канала вам
необходимо знать её id и указать его в URL запроса."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/chats/{id}', {'id': id})
        response = await client.get(url)
        response.raise_for_status()
    return response.json()


async def post_members_to_chats(self, id: int):
    """добавление пользователей в состав участников

Метод для добавления пользователей в состав участников беседы или канала."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/chats/{id}/members', {'id': id})
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def post_tags_to_chats(self, id: int):
    """добавление тегов в состав участников беседы или канала

Метод для добавления тегов в состав участников беседы или канала."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/chats/{id}/group_tags', {'id': id})
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def leave_chat(self, id: int):
    """Выход из беседы или канала

Метод для самостоятельного выхода из беседы или канала."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/chats/{id}/leave', {'id': id})
        response = await client.delete(url)
        response.raise_for_status()
    return response.json()


async def create_thread(self, id: int):
    """Создание нового треда

Этот метод позволяет создать новый тред к сообщению. Если у сообщения уже был
создан тред, то в ответе вернётся информация об уже созданном ранее треде."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/messages/{id}/thread', {'id': id})
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def create_message(self):
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
пользователями может быть только один личный чат."""
    client = await self.get_client()
    async with client:
        url = '/messages'
        response = await client.post(url)
        response.raise_for_status()
    return response.json()


async def edit_message(self, id: int):
    """Редактирование сообщения

Метод для редактирования сообщения или комментария."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/messages/{id}', {'id': id})
        response = await client.put(url)
        response.raise_for_status()
    return response.json()


async def delete_message_reactions(self, id: int, code: str = None):
    """Удаление реакции

Метод для удаления реакции на сообщение.  Удалить можно только те реакции,
которые были поставлены авторизованным пользователем."""
    client = await self.get_client()
    async with client:
        url = self.format_url('/messages/{id}/reactions', {'id': id})
        response = await client.delete(url, params={ 'code': code })
        response.raise_for_status()
    return response.json()


async def create_task(self):
    """Метод для создания нового напоминания.

При создании напоминания обязательным условием является указания типа
напоминания: звонок, встреча, простое напоминание, событие или письмо.  При
этом не требуется дополнительное описание - вы просто создадите напоминание с
соответствующим текстом. Если вы укажите описание напоминания - то именно оно и
станет текстом напоминания. У напоминания должны быть ответственные, если их не
указывать - ответственным назначаетесь вы."""
    client = await self.get_client()
    async with client:
        url = '/tasks'
        response = await client.post(url)
        response.raise_for_status()
    return response.json()
