import asyncio

def awaitme(f):
    """
    Decorator to handle synchronous and asynchronous functions.

    This decorator allows a function to work seamlessly with both
    synchronous and asynchronous code. If the function `f` is a coroutine
    (asynchronous), it will await the result. Otherwise, it will treat
    it as a regular synchronous function and return the result directly.

    :param f: The function to be decorated, which could be either synchronous or asynchronous.
    :type f: function
    :return: A wrapper function that handles the asynchronous behavior.
    :rtype: function

    :Example:

    #>>> @awaitme
    #>>> def sync_func():
    #>>>     return 42
    #>>> sync_func()
    42

    #>>> @awaitme
    #>>> async def async_func():
    #>>>     return 42
    #>>> await async_func()
    42
    """
    async def _awaitme(*args, **kwargs):
        func = f(*args, **kwargs)
        if asyncio.iscoroutine(func):
            return await func
        return func

    return _awaitme
