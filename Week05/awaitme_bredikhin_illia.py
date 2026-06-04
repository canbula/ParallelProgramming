def awaitme(func):
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__
    return wrapper
