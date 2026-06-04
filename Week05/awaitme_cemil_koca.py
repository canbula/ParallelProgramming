def awaitme(fn):
    async def _wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    _wrapper.__name__ = fn.__name__
    _wrapper.__doc__ = fn.__doc__
    _wrapper.__annotations__ = fn.__annotations__
    return _wrapper