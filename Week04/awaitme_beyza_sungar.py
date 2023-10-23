import asyncio

def coroutine_decorator(func):
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result

    return wrapper
