import asyncio


async def my_coroutine():
    print("Starting coroutine")
    await asyncio.sleep(0)
    print("Ending coroutine")


class AwaitableClass:
    def __await__(self):
        print("Awaiting")
        yield
        print("Done")


async def main():
    print("Starting main")
    await my_coroutine()
    await AwaitableClass()
    awaitable_object = AwaitableClass()
    await awaitable_object
    print("Ending main")


if __name__ == "__main__":
    asyncio.run(main())
