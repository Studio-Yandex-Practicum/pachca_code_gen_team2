import asyncio
from bot import PachcaBot, TOKEN

if __name__ == '__main__':

    print(id(PachcaBot))
    print(PachcaBot)
    pachca = PachcaBot(token=TOKEN)

    print(hasattr(pachca, 'get_common_methods'))

    async def run_pachca():
        print(await pachca.get_employee(id=514505))
        print(await pachca.get_employees())
        print(await pachca.get_tags())
        print(await pachca.get_tags_employees(id=27470))
        #print(await pachca.get_common_methods()) #Возвращает ошибку, нужно прописать обработку если (parameters.query и parameters.required)

    asyncio.run(run_pachca())

    print(type(pachca))
    print(pachca.__class__)
    print(pachca.__class__.__class__)
    print(pachca.__class__.__class__.__class__)
