def awaitme(func):
    """
    A decorator that turns any function into a coroutine.

    :param func: The function to be decorated.
    :type func: callable
    :return: An asynchronous wrapper of the function.
    :rtype: callable
    """
    async def _awaitme(*args, **kwargs):
        return func(*args, **kwargs)

    return _awaitme
