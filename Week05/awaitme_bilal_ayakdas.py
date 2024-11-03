import asyncio

def awaitme(fn):
    """
    Decorator to ensure synchronous and asynchronous functions can be awaited consistently.

    This decorator wraps a function, checking if it returns a coroutine. If so, it awaits the coroutine,
    allowing synchronous functions to run as usual while enabling asynchronous support.

    :param fn: The function to be decorated. Can be synchronous or asynchronous.
    :type fn: callable
    :return: A coroutine function that awaits the result if needed.
    :rtype: coroutine

    """

    async def convert_to_coroutine(*args, **kwargs):
        _func = fn(*args, **kwargs)
        if asyncio.iscoroutine(_func):
            return await _func
        return _func
    return convert_to_coroutine
