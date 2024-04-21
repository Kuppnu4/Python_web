import sys
from datetime import datetime, timedelta

import httpx
import asyncio
import platform


class HttpError(Exception):
    pass


async def request(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        # test = await client.get("https://github.com")
        # print(test.text)
        if r.status_code == 200:
            result = r.json()
            return result
        else:
            raise HttpError(f"Error status: {r.status_code} for {url}")


async def main(ind_day: int):
    # d = datetime.now() - timedelta(days=2) -> d.strftime('%d.%m.%Y')
    d = datetime.now() - timedelta(days=ind_day)
    shift = d.strftime('%d.%m.%Y')
    print(d)
    try:
        response = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={shift}')
        print(type(response))
        return response['exchangeRate']
    except HttpError as err:
        print(err)
        return None


if __name__ == '__main__':
    if platform.system() == 'Windows':

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print(sys.argv)
    r = asyncio.run(main(int(sys.argv[1])))
    print(r)