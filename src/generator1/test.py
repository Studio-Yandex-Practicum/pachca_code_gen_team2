from pydantic.dataclasses import dataclass


@dataclass
class Test:
    test1: int


test = Test(test1='123')
print(type(test.test1))
