import asyncio

def awaitme(func):
    async def wrapped(*a, **kw):
        if asyncio.iscoroutinefunction(func):
            return await func(*a, **kw)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, func, *a)
    return wrapped
