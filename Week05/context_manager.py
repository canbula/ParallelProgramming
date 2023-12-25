import asyncio


class ContextManager:
    def __init__(self) -> None:
        print(f"Initializing {self.__class__.__name__}")

    def __enter__(self) -> "ContextManager":
        print(f"Entering {self.__class__.__name__}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(f"Exiting {self.__class__.__name__}")
        print(f"e: {exc_type}, v: {exc_val}, tb: {exc_tb}")
        return True

    def __call__(self, task: str) -> None:
        print(f"Calling {task}")
        return None


class AsyncContextManager:
    def __init__(self) -> None:
        print(f"Initializing {self.__class__.__name__}")

    async def __aenter__(self) -> "AsyncContextManager":
        print(f"Entering {self.__class__.__name__}")
        await asyncio.sleep(0)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(f"Exiting {self.__class__.__name__}")
        print(f"e: {exc_type}, v: {exc_val}, tb: {exc_tb}")
        await asyncio.sleep(0)
        return True

    async def __call__(self, task: str) -> None:
        print(f"Calling {task}")
        await asyncio.sleep(0)
        return None


def main() -> None:
    with ContextManager() as cm:
        cm("example task")


async def async_main() -> None:
    async with AsyncContextManager() as acm:
        await acm("example task")


if __name__ == "__main__":
    main()
    asyncio.run(async_main())
