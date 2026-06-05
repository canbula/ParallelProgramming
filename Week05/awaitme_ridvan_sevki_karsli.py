import inspect

def awaitme(func):
    async def wrapper(*args, **kwargs):
        if inspect.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
