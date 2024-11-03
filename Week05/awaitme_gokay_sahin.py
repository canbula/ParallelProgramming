import asyncio


def awaitme(func):
    """
    Converts a function into a coroutine.

    :return: Coroutine version of the function.
    :rtype: Coroutine
    """
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if asyncio.iscoroutine(result):
            return await result
        else:
            return result
        
    return wrapper
