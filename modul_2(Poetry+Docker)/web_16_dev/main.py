from typing import TypedDict, Literal, NamedTuple
from dataclasses import dataclass


class UserInfo(TypedDict):
    id: int
    user_name: str
    email: str
    is_active: bool

@dataclass(frozen=True)
class UserSchema:
    id: int
    user_name: str
    email: str
    is_active: bool


class Cat(NamedTuple):
    nick: str
    age: int


User = {
    'id': 123,
    'user_name': 'Aleks',
    'email': 'asdaleks@asd.asd',
    'is_active': True
}


def get_user() -> UserInfo:
    return User


def get_user_info() -> UserSchema:
    return UserSchema(id=123, user_name='Aleks', email='asdaleks@asd.asd', is_active=True)


def my_mul(data: list) -> float:
    result = 1
    for n in data:
        result = result * n
    return result


Shape = Literal['circle', 'square']


def foo(shape):
    if shape == 'circle':
        print('circle')
    if shape == 'square':
        print('square')


if __name__ == '__main__':
    my_mul([2])
    print(get_user()['user_name'])
    cat = Cat('Simon', 5)
    print(cat.nick)

