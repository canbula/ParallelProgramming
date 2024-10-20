import asyncio

def awaitme(func):
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Check if the result is a coroutine and await it if necessary
        if asyncio.iscoroutine(result):
            return await result
        return result

    # This ensures the decorated function can be used both synchronously and asynchronously
    if asyncio.iscoroutinefunction(func):
        return wrapper
    else:
        # If it's not a coroutine function, return the original function
        return func
