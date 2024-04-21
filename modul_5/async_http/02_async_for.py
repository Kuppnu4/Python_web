import asyncio
from faker import Faker
from typing import Iterable, Awaitable, Coroutine, Any

from timing import async_timed

fake = Faker("uk-UA")


async def async_get_user_fm_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def get_users(uuids: list[int]) -> list[Coroutine[int, Any, dict]]:
    return [async_get_user_fm_db(pk) for pk in uuids]


@async_timed('----------------------main---------------------')
async def main(users: Coroutine[int, Any, list[Coroutine[int, Any, dict]]]):
    users_ = [user for user in await users]
    result = await asyncio.gather(*users_)
    return result


if __name__ == "__main__":
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
