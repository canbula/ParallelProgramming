import functools

def awaitme(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
