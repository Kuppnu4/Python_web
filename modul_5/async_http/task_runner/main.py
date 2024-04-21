import asyncio
import logging
from random import randint
from timing import async_timed

from aiopath import AsyncPath
from aiofile import async_open


async def producer(file: AsyncPath, q: asyncio.Queue):
    async with async_open(file, 'r', encoding='utf-8') as afd:
        data = []
        async for line in afd:
            data.append(line)
        await q.put((file, ''.join(data)))


async def consumer(filename, q: asyncio.Queue):
    async with async_open(filename, 'w', encoding='utf-8') as afd:
        while True:
            file, blob = await q.get()
            logging.info(f'Write file {file.name} -- {blob}')
            await afd.write(f'{blob}\n')
            q.task_done()


@async_timed('_____main______')
async def main():

    queue_files = asyncio.Queue()
    list_files = AsyncPath('.').joinpath('files').glob('*.js')

    loop = asyncio.get_running_loop()
    consumer_task = loop.create_task(consumer('main.js', queue_files))

    producer_tasks = [loop.create_task(producer(file, queue_files)) async for file in list_files]
    await asyncio.gather(*producer_tasks)
    await queue_files.join()
    consumer_task.cancel()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    asyncio.run(main())
