"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import aiohttp
import time


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()

# urls = [
#     USERS_DATA_URL,
#     POSTS_DATA_URL,
# ]

# async def main():
#     results = await asyncio.gather(*[fetch(url) for url in urls])
#     print(results)

# asyncio.run(main())

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html1 = await fetch(session, USERS_DATA_URL)
        html2 = await fetch(session, POSTS_DATA_URL)
        print(html1)
        print(html2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())