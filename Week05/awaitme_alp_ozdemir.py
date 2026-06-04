def awaitme(func):
    async def init(*args,**kwargs):
        res = func(*args,**kwargs)
        return res
    return init
