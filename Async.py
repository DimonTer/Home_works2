import asyncio


async def sek(t: int):
    for i in range(1, t + 1):
        await asyncio.sleep(1)
        print(f' left  {i}  sec')


async def main():
    t1 = asyncio.create_task(sek(3))
    t2 = asyncio.create_task(sek(3))
    t3 = asyncio.create_task(sek(3))
    t4 = asyncio.create_task(sek(3))
    t5 = asyncio.create_task(sek(3))
    await t1
    await t2
    await t3
    await t4
    await t5

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


