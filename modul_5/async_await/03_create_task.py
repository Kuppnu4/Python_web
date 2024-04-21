import asyncio
from time import sleep, time
from faker import Faker

fake = Faker("uk-UA")


# Awaitable -> Coroutine
# Awaitable -> Future -> Task


async def async_get_user_fm_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 6):
        task = asyncio.create_task(async_get_user_fm_db(i))
        users.append(task)
    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":

    start = time()
    users = asyncio.run(main())
    # run() - performs next 3 lines
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # users = loop.run_until_complete(main())
    print(users)
    print(time() - start)
