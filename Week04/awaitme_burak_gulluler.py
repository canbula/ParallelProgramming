import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper
