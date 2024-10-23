import asyncio

def awaitme(function):
    async def _awaitme(*args, **kwargs):
        func = function(*args, **kwargs)
        if asyncio.iscoroutine(func):
            return await func
        return func
    return _awaitme
