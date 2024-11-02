import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        if not asyncio.iscoroutinefunction(func):
            return func(*args,**kwargs)
        return await func(*args,**kwargs)
    return wrapper
