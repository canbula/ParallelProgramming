import asyncio


async def a():
    print("a start")
    await asyncio.sleep(1)
    print("a end")


async def b():
    print("b start")
    await asyncio.sleep(1)
    print("b end")


async def c():
    print("c start")
    await asyncio.sleep(1)
    print("c end")


async def d():
    print("d start")
    await asyncio.sleep(1)
    print("d end")


async def e():
    print("e start")
    await asyncio.sleep(3)
    print("e end")


async def f():
    print("f start")
    await asyncio.sleep(3)
    print("f end")


async def g():
    print("g start")
    await asyncio.sleep(8)
    print("g end")


async def ab():
    await a()
    await b()


async def cd():
    await c()
    await d()


async def eab():
    await asyncio.gather(*[asyncio.create_task(e()), asyncio.create_task(ab())])


async def fcd():
    await asyncio.gather(*[asyncio.create_task(f()), asyncio.create_task(cd())])


async def ef():
    await eab()
    await fcd()


async def main() -> None:
    print("main start")
    await asyncio.gather(*[asyncio.create_task(g()), asyncio.create_task(ef())])
    print("main end")
    return None


if __name__ == '__main__':
    asyncio.run(main())
