import asyncio


async def simple_coroutine(func: list[callable], t: int) -> None:
    print(f"Starting coroutine with {t} seconds delay")
    await asyncio.sleep(t)
    for f in func:
        f()
    await asyncio.sleep(t)
    print(f"Finished coroutine with {t} seconds delay")


def func_1():
    s = 0
    for _ in range(10000):
        s += 1
    print("Finished func_1")


def func_2():
    s = 0
    for _ in range(10000):
        s += 1
    print("Finished func_2")


async def async_main():
    coroutine_1 = simple_coroutine([func_1, func_2], 1)
    coroutine_2 = simple_coroutine([], 5)
    await asyncio.gather(coroutine_1, coroutine_2)

if __name__ == "__main__":
    asyncio.run(async_main())
