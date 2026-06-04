from functools import wraps
from inspect import isawaitable


def awaitme(func):
    # Preserve original function metadata (name, docstring, etc.)
    @wraps(func)
    async def inner(*args, **kwargs):
        # Call the original function with given arguments
        value = func(*args, **kwargs)

        # Check if the returned value can be awaited (e.g., coroutine, future)
        if isawaitable(value):
            # Await the result if it is awaitable
            return await value

        # Otherwise, return the result directly
        return value

    # Return the async wrapper function
    return inner
