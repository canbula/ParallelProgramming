import asyncio

def awaitme(f):
    async def _awaitme(*args, **kwargs):
        return_value = f(*args, **kwargs)
        if return_value != None:
            return return_value
    return _awaitme
