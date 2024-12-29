import asyncio
from gen_class_pachca import PachcaBot

if __name__ == '__main__':

    print(id(PachcaBot))

    pachca = PachcaBot()

    print(hasattr(pachca, 'client'))

    #print(hasattr(pachca, 'get_custom_properties'))

    async def run_pachca():
        print(await pachca.get_employee(id=514505))
        print(await pachca.get_employees(param_query={'per': 1}))
        print(await pachca.get_tags())
        print(await pachca.get_tags_employees(id=27470))
        print(await pachca.get_common_methods()) #Возвращает ошибку, нужно прописать обработку если (parameters.query и parameters.required)

    asyncio.run(run_pachca())

    print(type(pachca))
    print(pachca.__class__.__name__)