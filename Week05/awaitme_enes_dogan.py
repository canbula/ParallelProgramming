import asyncio

def awaitme(function):
    async def _awaitme(*args, **kwargs):
        result = function(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result
    return _awaitme
