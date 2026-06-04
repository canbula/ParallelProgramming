import asyncio

def awaitme(fn):
    async def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        return result
    return wrapper