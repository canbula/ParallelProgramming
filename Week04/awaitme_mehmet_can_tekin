import asyncio


def awaitme(func):
    async def _awaitme(*args,**kwargs):
        result =func(*args,**kwargs)
        if asyncio.iscoroutinefunction(result):
            return await result
        else:
            return result
    return _awaitme



