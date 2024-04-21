import asyncio
from faker import Faker
from typing import Iterable, Awaitable

from timing import async_timed

fake = Faker("uk-UA")


async def async_get_user_fm_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


def get_users(uuids: list[int]) -> Iterable[Awaitable]:
    return [async_get_user_fm_db(pk) for pk in uuids]


@async_timed('----------------------main---------------------')
async def main(users: Iterable[Awaitable]):
    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
