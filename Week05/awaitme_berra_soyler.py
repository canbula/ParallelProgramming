import asyncio
from functools import wraps

def awaitme(func):
   @wraps(func)
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if asyncio.iscoroutine(result):
            return await result
        else:
            return result

    return wrapper
