def awaitme(func):
    async def init(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return init
