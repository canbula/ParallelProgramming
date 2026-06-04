import asyncio
def awaitme(fn):
    async def wrapper(*args,**kwargs):
        value = fn(*args,**kwargs)
        if asyncio.iscoroutine(fn):
            return await value
        return value
    return wrapper



        
