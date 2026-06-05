import asyncio


def awaitme(func):
    async def wrapper(*args, **kwargs):
        await asyncio.sleep(0)
        return func(*args, **kwargs)

    return wrapper