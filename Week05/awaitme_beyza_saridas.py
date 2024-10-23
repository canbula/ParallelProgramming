import asyncio

def coroutine_decorator(func):
    async def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if asyncio.iscoroutine(result):
            return await result
        
        return result
