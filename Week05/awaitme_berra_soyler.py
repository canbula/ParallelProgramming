import asyncio

def awaitme(func):
    async def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if asyncio.iscoroutine(result):
            return await result
        else:
            return result

    return wrap
