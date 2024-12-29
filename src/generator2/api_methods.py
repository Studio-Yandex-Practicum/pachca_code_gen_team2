"""Сгенерированные методы запроса."""


async def get_common_methods(self, param_query=None):
    """Список дополнительных полей

Метод для получения актуального списка дополнительных полей участников и напоминаний в вашей компании.
"""
    client = await self.get_client()
    async with client:
        response = await client.get('/custom_properties', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_uploads(self, param_query=None):
    """Получение подписи и ключа для загрузки файла

Возвращает параметры, необходимые для безопасной загрузки файла."""
    client = await self.get_client()
    async with client:
        response = await client.post('/uploads', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_direct_url(self, param_query=None):
    """Получение URL для загрузки

Отправляет запрос для получения URL для безопасной загрузки файла."""
    client = await self.get_client()
    async with client:
        response = await client.post('/direct_url', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_employees(self, param_query=None):
    """получение актуального списка всех сотрудников компании

Fetch a paginated list of employees with optional filtering by query.
"""
    client = await self.get_client()
    async with client:
        response = await client.get('/users', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_employee(self, id, param_query=None):
    """получение информации о сотруднике

Метод для получения информации о сотруднике.
Для получения сотрудника вам необходимо знать его id и указать его в URL запроса.
"""
    client = await self.get_client()
    async with client:
        response = await client.get(f'/users/{id}', params=param_query)
        response.raise_for_status()
    return response.json()


async def del_status(self, param_query=None):
    """удаление своего статуса

Параметры запроса отсутствуют
"""
    client = await self.get_client()
    async with client:
        response = await client.delete('/profile/status', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_tag(self, id, param_query=None):
    """Информация о теге

Параметры запроса отсутствуют
"""
    client = await self.get_client()
    async with client:
        response = await client.get(f'/group_tags/{id}', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_tags(self, param_query=None):
    """Список тегов сотрудников

Метод для получения актуального списка тегов сотрудников.
"""
    client = await self.get_client()
    async with client:
        response = await client.get('/group_tags', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_tags_employees(self, id, param_query=None):
    """получение актуального списка сотрудников тега

Метод для получения актуального списка сотрудников тега.
"""
    client = await self.get_client()
    async with client:
        response = await client.get(f'/group_tags/{id}/users', params=param_query)
        response.raise_for_status()
    return response.json()


async def create_chat(self, param_query=None):
    """Новая беседа или канал

Метод для создания новой беседы или нового канала.
При создании беседы или канала вы автоматически становитесь участником.\
"""
    client = await self.get_client()
    async with client:
        response = await client.post('/chats', params=param_query)
        response.raise_for_status()
    return response.json()


async def get_chat(self, id, param_query=None):
    """Информация о беседе или канале

Получения информации о беседе или канале.
Для получения беседы или канала вам необходимо знать её id и указать его в URL запроса.
"""
    client = await self.get_client()
    async with client:
        response = await client.get(f'/chats/{id}', params=param_query)
        response.raise_for_status()
    return response.json()


async def post_members_to_chats(self, id, param_query=None):
    """добавление пользователей в состав участников

Метод для добавления пользователей в состав участников беседы или канала.
"""
    client = await self.get_client()
    async with client:
        response = await client.post(f'/chats/{id}/members', params=param_query)
        response.raise_for_status()
    return response.json()


async def post_tags_to_chats(self, id, param_query=None):
    """добавление тегов в состав участников беседы или канала

Метод для добавления тегов в состав участников беседы или канала.
"""
    client = await self.get_client()
    async with client:
        response = await client.post(f'/chats/{id}/group_tags', params=param_query)
        response.raise_for_status()
    return response.json()


async def leave_chat(self, id, param_query=None):
    """Выход из беседы или канала

Метод для самостоятельного выхода из беседы или канала."""
    client = await self.get_client()
    async with client:
        response = await client.delete(f'/chats/{id}/leave', params=param_query)
        response.raise_for_status()
    return response.json()


async def create_thread(self, id, param_query=None):
    """Создание нового треда

Этот метод позволяет создать новый тред к сообщению. Если у сообщения уже был создан тред, то в ответе вернётся информация об уже созданном ранее треде.
"""
    client = await self.get_client()
    async with client:
        response = await client.post(f'/messages/{id}/thread', params=param_query)
        response.raise_for_status()
    return response.json()


async def create_message(self, param_query=None):
    """создание нового сообщения

Метод для отправки сообщения в беседу или канал,
личного сообщения пользователю или комментария в тред.

При использовании entity_type: "discussion" (или просто без указания entity_type)
допускается отправка любого chat_id в поле entity_id.
То есть, сообщение можно отправить зная только идентификатор чата.
При этом, вы имеете возможность отправить сообщение в тред по его идентификатору
или личное сообщение по идентификатору пользователя.

Для отправки личного сообщения пользователю создавать чат не требуется. 
Достаточно указать entity_type: "user" и идентификатор пользователя. 
Чат будет создан автоматически, если между вами ещё не было переписки.
Между двумя пользователями может быть только один личный чат.
"""
    client = await self.get_client()
    async with client:
        response = await client.post('/messages', params=param_query)
        response.raise_for_status()
    return response.json()


async def edit_message(self, id, param_query=None):
    """Редактирование сообщения

Метод для редактирования сообщения или комментария."""
    client = await self.get_client()
    async with client:
        response = await client.put(f'/messages/{id}', params=param_query)
        response.raise_for_status()
    return response.json()


async def delete_message_reactions(self, id, param_query=None):
    """Удаление реакции

Метод для удаления реакции на сообщение.  Удалить можно только те реакции, которые были поставлены авторизованным пользователем.
"""
    client = await self.get_client()
    async with client:
        response = await client.delete(f'/messages/{id}/reactions', params=param_query)
        response.raise_for_status()
    return response.json()


async def create_task(self, param_query=None):
    """Метод для создания нового напоминания.

При создании напоминания обязательным условием является указания типа напоминания: звонок, встреча, простое напоминание, событие или письмо. 
При этом не требуется дополнительное описание - вы просто создадите напоминание с соответствующим текстом.
Если вы укажите описание напоминания - то именно оно и станет текстом напоминания.
У напоминания должны быть ответственные, если их не указывать - ответственным назначаетесь вы.
"""
    client = await self.get_client()
    async with client:
        response = await client.post('/tasks', params=param_query)
        response.raise_for_status()
    return response.json()

