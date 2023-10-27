import asyncio

def awaitme(func):
    async def _awaitme(*args, **kwargs):
        return_value = func(*args, **kwargs)
        if asyncio.iscoroutine(return_value):
            return await return_value
        else:
            return return_value

    return _awaitme
