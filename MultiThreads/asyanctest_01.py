import asyncio
import aiohttp

async def async_crwaw(url):
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url},{len(result)}")

loop =asyncio.get_event_loop()

# tasks = [for url in ]
