import asyncio
from random import randint
from timing import async_timed


async def producer(q: asyncio.Queue):
    num = randint(1, 1_000_000)
    await asyncio.sleep(0.1)
    await q.put(num)


async def consumer(q: asyncio.Queue):
    while True:
        num = await q.get()
        print(num ** 2)
        q.task_done()


@async_timed('_____main______')
async def main():
    queue = asyncio.Queue()
    loop = asyncio.get_running_loop()
    consumer_tasks = [loop.create_task(consumer(queue)) for _ in range(3)]
    producer_tasks = [loop.create_task(producer(queue)) for _ in range(1_000_000)]
    await asyncio.gather(*producer_tasks)
    await queue.join()
    [task.cancel() for task in consumer_tasks]


if __name__ == '__main__':
    asyncio.run(main())