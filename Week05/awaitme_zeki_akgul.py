import asyncio, inspect

def awaitme(func):
    async def wrapper(*args, **kwargs):        
        result = func(*args, **kwargs)
        if inspect.iscoroutinefunction(func):
            return await result
        return result
    return wrapper
