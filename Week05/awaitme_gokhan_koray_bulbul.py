import asyncio

def awaitme(givenFunction):
    if asyncio.iscoroutinefunction(givenFunction):
        return givenFunction

    async def wrapper(*args, **kwargs):
        return givenFunction(*args, **kwargs)

    return wrapper
