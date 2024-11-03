import asyncio

def awaitme(f):
    """
    A decorator to handle both synchronous and asynchronous functions seamlessly.

    If the decorated function is asynchronous, it awaits the function's result.
    If the decorated function is synchronous, it directly returns the result.

    Args:
        f (function): The function to be decorated. It can be either synchronous or asynchronous.

    Returns:
        function: An asynchronous wrapper that handles both sync and async functions gracefully.
    """
    async def wrapper(*args, **kwargs):
        """
        Wrapper function that calls the original function and checks whether it's a coroutine.

        If the result is a coroutine, it awaits the result. Otherwise, it returns the result directly.

        Args:
            *args: Positional arguments to pass to the original function.
            **kwargs: Keyword arguments to pass to the original function.

        Returns:
            Any: The result of the original function, either awaited (if async) or direct (if sync).
        """
        fn = f(*args, **kwargs)
        if asyncio.iscoroutine(fn):
            return await fn
        return fn

    return wrapper
