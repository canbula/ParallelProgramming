import asyncio

def async_handler(func):
    async def wrapper(*args, **kwargs):
        outcome = func(*args, **kwargs)
        if asyncio.iscoroutine(outcome):
            return await outcome
        return outcome
    return wrapper
