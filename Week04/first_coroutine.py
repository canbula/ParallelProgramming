import asyncio
import time


async def my_coroutine():
    print("Starting coroutine")
    await asyncio.sleep(1)
    print("Ending coroutine")

def function_1():
    print("F1: Starting function")
    time.sleep(5)
    print("F1: Ending function")

def function_2():
    print("F2: Starting function")
    time.sleep(2)
    print("F2: Ending function")

def sync_main():
    print("Sync: Starting main")
    function_1()
    function_2()
    print("Sync: Ending main")

async def coroutine_1():
    print("C1: Starting coroutine")
    await asyncio.sleep(5)
    print("C1: Ending coroutine")

async def coroutine_2():
    print("C2: Starting coroutine")
    await asyncio.sleep(2)
    print("C2: Ending coroutine")

async def async_main():
    print("Async: Starting main")
    await asyncio.gather(coroutine_1(), coroutine_2()) # gather more than one coroutine
    print("Async: Ending main")


if __name__ == "__main__":
    # my_coroutine() # coroutine 'my_coroutine' was never awaited
    # await my_coroutine() # SyntaxError: 'await' outside async function
    asyncio.run(my_coroutine()) # Standard way to run a coroutine
    print(type(my_coroutine)) # <class 'function'>
    print(type(my_coroutine())) # <class 'coroutine'>
    # Event loop
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(my_coroutine())
    # loop.close()

    # Sync
    sync_main()
    # Async
    asyncio.run(async_main())
