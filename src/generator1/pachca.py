import asyncio

from pachca_api_open_api_3_0_client.client import Pachca
from pachca_api_open_api_3_0_client.models.create_chat_body import (
    CreateChatBody,
)
from pachca_api_open_api_3_0_client.models.query_chat import QueryChat
from pachca_api_open_api_3_0_client.models.edit_messages import EditMessages
from pachca_api_open_api_3_0_client.models.create_message import (
    CreateMessage)
from pachca_api_open_api_3_0_client.models.create_message_body import (
    CreateMessageBody)
from pachca_api_open_api_3_0_client.models.edit_message_body import (
    EditMessageBody)
from pachca_api_open_api_3_0_client.models.get_message_reactions_body import (
    GetMessageReactionsBody)

query_chat = QueryChat(name='Testing')

chat_body = CreateChatBody(chat=query_chat)

create_meassage = CreateMessage(
    entity_id=1781540, content='NOT SUPER PUPER2222')

edit_meassage = EditMessages(content='NOT and NOT SUPER PUPER')

edit_message_body = EditMessageBody(message=edit_meassage)

reaction_body = GetMessageReactionsBody()

message_body = CreateMessageBody(message=create_meassage)

pachca = Pachca(
    token='qW3V2Kw7yxu1UA5OZLCdyoyKFfWA6OYr_MK2WR6PxbA',
)


async def main() -> None:
    """Функция теста эндпоинтов"""

    task3 = asyncio.create_task(pachca.deleteMessageReactions(
        id=412338865, code='😭'))
    task6 = asyncio.create_task(
        pachca.postMessageReactions(412338865, body=reaction_body))


    print(await task3)
    print('*' * 30)
    print(await task6)



if __name__ == '__main__':
    asyncio.run(main())