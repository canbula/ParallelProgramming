import asyncio

def awaitme(func):
    async def _awaitme(*args,**kwargs):
        asyncio.run(func(*args,**kwargs))
    return _awaitme
