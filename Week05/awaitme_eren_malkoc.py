import asyncio

def awaitme(fn):
    async def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        else:
            return result  

    return wrapper  
