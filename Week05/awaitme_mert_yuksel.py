def awaitme(func):

    async def _awaitme(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    
    return _awaitme