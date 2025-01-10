import asyncio

from .bot import Bot
from .models.models_reqBod_createMessage import Createmessage, Message

if __name__ == '__main__':

    print(id(Bot))
    print(Bot)
    pachca = Bot(token='Bearer 35KekGygDNiFwtPpqUe44CaEZ_EVL17ycYRJrMnvHOs')

    print(pachca.token)
    print(hasattr(pachca, 'get_common_methods'))

    message_test = Createmessage(message=Message(
        entity_type="discussion",
        entity_id=17579010,
        content="Вчера мы продали 756 футболок (что на 10% больше, чем в прошлое воскресенье)",
    ))
    #print(message_test.model_dump())
    async def run_pachca():
        print(await pachca.get_employee(id=514505))
        print(await pachca.get_employees())
        print(await pachca.get_tags())
        print(await pachca.get_tags_employees(id=27470))
        print(await pachca.get_chats(per=2))
        message = await pachca.create_message(data=message_test)
        print(message)
        #print(await pachca.get_common_methods()) #Возвращает ошибку, нужно прописать обработку если (parameters.query и parameters.required)

    asyncio.run(run_pachca())

    print(type(pachca))
    print(pachca.__class__)
    print(pachca.__class__.__class__)
    print(pachca.__class__.__class__.__class__)