def awaitme(fn):
    async def _fn(*args, **kwargs):
        return fn(*args, **kwargs)
    return _fn
