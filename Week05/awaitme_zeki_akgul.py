import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):        
        result = func(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result
    return wrapper
