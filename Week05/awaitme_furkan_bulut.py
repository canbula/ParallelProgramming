import asyncio

def awaitme(f):
    async def _awaitme(*args,**kwargs):
        func = f(*args,**kwargs)
        if asyncio.iscoroutine(func):
            return await func
        return func
    return _awaitme
