import asyncio


def awaitme (func):
    """
    A decorator that transforms a regular function into a coroutine.

    If the function is already a coroutine function, it will be awaited directly.
    If it is a regular (synchronous) function, the decorator will check for the
    current event loop and run the function in an executor. If there is no
    current event loop, it will create a new event loop and run the function
    there.

    This allows both synchronous and asynchronous functions to be used in an
    asynchronous context seamlessly.

    :param func: The function to be transformed into a coroutine.
                 This can be either a coroutine function or a regular function.
    :type func: Callable
    :returns: The result of the function execution.
    :rtype: Any
    :raises RuntimeError: If there is an issue obtaining the current event loop,
                         the function will be executed in a new event loop instead
                         without raising an error.
    """

    async def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
             try:
                 current_event_loop = asyncio.get_event_loop()
                 return await current_event_loop.run_in_executor(None, func, *args)
             except RuntimeError:
                 return await asyncio.run(func(*args, **kwargs))
    return wrapper
