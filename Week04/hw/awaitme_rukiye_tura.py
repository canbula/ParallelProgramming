import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        elif asyncio.isfuture(result):
            return await asyncio.wrap_future(result)
        return result

    return wrapper
