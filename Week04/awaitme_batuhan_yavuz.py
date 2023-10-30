import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        if inspect.iscoroutinefunction(func):
            return await func(*args,**kwargs)
        else:
            return func(*args,**kwargs)
    return wrapper
