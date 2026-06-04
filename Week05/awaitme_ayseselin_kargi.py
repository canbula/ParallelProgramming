import asyncio

def awaitme(fn):
    if asyncio.iscoroutinefunction(fn):
        return fn

    async def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    try:
        wrapper.__name__ = fn.__name__
        wrapper.__doc__ = fn.__doc__
        wrapper.__annotations__ = fn.__annotations__
    except (AttributeError, TypeError):
        pass

    return wrapper
