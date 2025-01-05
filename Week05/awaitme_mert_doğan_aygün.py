import asyncio


def make_async(func):
    """
    A decorator to convert a function into a coroutine.

    If the function is already a coroutine function, it will be awaited.
    If the function is synchronous, it will be executed in an executor 
    within the current event loop or in a new event loop if none is available.

    This ensures compatibility between synchronous and asynchronous 
    functions in an async context.

    :param func: The target function (can be synchronous or asynchronous).
    :type func: Callable
    :return: The result of the function execution.
    :rtype: Any
    """

    async def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        try:
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, func, *args)
        except RuntimeError:  # No current event loop
            return await asyncio.to_thread(func, *args)

    return wrapper
