import asyncio
from functools import wraps

def awaitme(func):
    """
    A decorator that turns any function into a coroutine.
    It passes all arguments to the function and returns its output.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Check if the function is already an asynchronous coroutine
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        
        # If it is a synchronous function, run it in a separate thread
        # so it behaves as a non-blocking awaitable coroutine
        return await asyncio.to_thread(func, *args, **kwargs)

    return wrapper
