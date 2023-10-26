import asyncio


def awaitme(func):
    async def coroutine(*args, **kwargs):

        result = func(*args, **kwargs)
        if asyncio.iscoroutinefunction(func):
            return await result
        else:
            return result

    return coroutine
