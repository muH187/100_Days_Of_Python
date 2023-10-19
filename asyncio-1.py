import asyncio

async def func1():
    task = asyncio.create_task(func2())
    print('a')
    await asyncio.sleep(2)
    print('b')

async def func2():
    print('c')
    await asyncio.sleep(3)
    print('d')

asyncio.run(func1())
