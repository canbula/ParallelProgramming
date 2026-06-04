import asyncio

def awaitme(function):
    async def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result
    return wrapper
