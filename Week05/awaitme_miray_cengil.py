import asyncio

def awaitme(func):
    """
    A decorator that turns any function into a coroutine.
    It properly passes all arguments to the function.
    If the function returns a value, the decorator will return it.
    """
    async def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, lambda: func(*args, **kwargs))
    
    return wrapper
