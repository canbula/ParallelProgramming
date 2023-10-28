import asyncio


def awaitme(function):
    async def coroutine(*args, **kwargs):

        result = function(*args, **kwargs)
        if asyncio.iscoroutinefunction(function):
            return await result
        else:
            return result

    return coroutine
