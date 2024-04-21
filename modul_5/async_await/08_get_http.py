import asyncio
import requests
from requests.exceptions import InvalidSchema, MissingSchema, SSLError

from concurrent.futures import ThreadPoolExecutor

from timing import async_timed, sync_timed

urls = [
    "https://github.com",
    "https://www.codewars.com",
    "https://rezka.cc",
    "https://hltv.org",
    "https://www.youtube.com",
    "https://tabletki.ua",
    "https://stackoverflow.com",
    "ws://test",
    "asssdfff",
]


def get_preview(url: str) -> tuple[str, str]:
    res = requests.get(url)
    return url, res.text[:25]


@sync_timed()
def main_synk():
    results = []
    for url in urls:
        try:
            results.append(get_preview(url))
        except (InvalidSchema, MissingSchema, SSLError) as err:
            print(err)

    return results


@async_timed()
async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(10) as pool:
        futures = [loop.run_in_executor(pool, get_preview, url) for url in urls]
        r = await asyncio.gather(*futures, return_exceptions=True)
        return r


if __name__ == "__main__":
    print(main_synk())

    r = asyncio.run(main())
    new_res = []
    for i in filter(lambda el: not isinstance(el, Exception), r):
        new_res.append(i)
    print(new_res)
