import asyncio
import time


def f1():
    print("F1: Start")
    time.sleep(5)
    print("F1: End")


def f2():
    print("F2: Start")
    time.sleep(2)
    print("F2: End")


def sync_main():
    print("Sync Main: Start")
    f1()
    f2()
    print("Sync Main: End")


async def c1():
    print("C1: Start")
    await asyncio.sleep(5)
    print("C1: End")


async def c2():
    print("C2: Start")
    await asyncio.sleep(2)
    print("C2: End")


async def async_main_inefficient():
    print("Async Main: Start")
    await c1()
    await c2()
    print("Async Main: End")


async def async_main_efficient():
    print("Async Main Efficient: Start")
    await asyncio.gather(c1(), c2())
    print("Async Main Efficient: End")


if __name__ == "__main__":
    start_time = time.time()
    sync_main()
    end_time = time.time()
    print(f"Time taken by sync_main: {(end_time - start_time):.2f} seconds")

    start_time = time.time()
    asyncio.run(async_main_inefficient())
    end_time = time.time()
    print(
        f"Time taken by async_main_inefficient: {(end_time - start_time):.2f} seconds"
    )

    start_time = time.time()
    asyncio.run(async_main_efficient())
    end_time = time.time()
    print(f"Time taken by async_main_efficient: {(end_time - start_time):.2f} seconds")
