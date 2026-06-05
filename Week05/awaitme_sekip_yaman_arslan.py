def awaitme(func):
    """
    A decorator that wraps a regular function as an async (coroutine) function.
    """

    async def _awaitme(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return _awaitme
