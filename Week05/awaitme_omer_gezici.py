import asyncio
import functools

def awaitme(func):
    @functools.wraps(fun)
    async def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result
    return wrapper
