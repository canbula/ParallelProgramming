import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        await func(*args, **kwargs)
    return wrapper
