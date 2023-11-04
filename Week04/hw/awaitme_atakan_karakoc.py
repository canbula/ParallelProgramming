import asyncio, inspect

def awaitme(function):
    async def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if inspect.iscoroutinefunction(function):
            return await result
        else:
            return result
    return wrapper
