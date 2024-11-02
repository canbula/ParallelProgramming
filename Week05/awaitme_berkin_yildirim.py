import asyncio
from functools import wraps

def awaitme(func):
    """
    Calls the given function and awaits if it's an async function,
    otherwise calls it normally.
    :param func: The function to be called.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result

    return wrapper
