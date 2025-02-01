import asyncio

def awaitme(func):
    """Decorator to handle both synchronous and asynchronous functions."""
    
    async def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result

    return _wrapper
