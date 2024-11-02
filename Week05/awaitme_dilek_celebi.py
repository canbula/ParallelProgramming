import asyncio
from functools import wraps

def awaitme(func):
    """
    A decorator that turns any function into a coroutine.
    It will pass all arguments to the function properly and return any value from the function.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Run the function in a separate thread if it's not a coroutine
        if not asyncio.iscoroutinefunction(func):
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, func, *args, **kwargs)
        # If it's already a coroutine, simply await it
        return await func(*args, **kwargs)
    return wrapper
