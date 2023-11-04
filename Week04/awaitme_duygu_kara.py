import asyncio

def awaitme(func):

    """
    The decorator which turns any function into a coroutine.
    It pass all the arguments to the function properly. 
    If function returns any value, so the decorator returns it.
    
    """
    async def _awaitme(*args, **kwargs):
        result = func(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        else :
            return result

    return _awaitme
