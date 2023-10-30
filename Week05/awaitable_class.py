import asyncio


async def my_coroutine():
    print(f"Starting coroutine")
    await asyncio.sleep(1)
    print(f"Ending coroutine")


class AwaitableClass:
    def __await__(self):
        print("Awaitable class starting")
        yield
        print("Awaitable class ending")


async def main():
    print(f"Starting main")
    await my_coroutine()
    await AwaitableClass()
    awaitable_object = AwaitableClass()
    await awaitable_object
    print(f"Ending main")


if __name__ == "__main__":
    asyncio.run(main())
