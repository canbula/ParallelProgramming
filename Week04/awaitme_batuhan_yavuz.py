import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return await return_value
    return wrapper
