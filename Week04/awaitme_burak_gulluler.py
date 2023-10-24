import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
