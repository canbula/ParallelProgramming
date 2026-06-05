import asyncio

def awaitme(func):
    
    async def wrapper(*args, **kwargs):
        
        return func(*args, **kwargs)
        
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    
    if hasattr(func, '__annotations__'):
        wrapper.__annotations__ = func.__annotations__
        
    return wrapper
