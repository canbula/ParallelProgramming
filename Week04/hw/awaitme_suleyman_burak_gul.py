import asyncio

def awaitmee(fn):
    async def _awaitmee(*args, **kwargs):
        result = fn(*args, **kwargs)
        if asyncio.iscoroutinefunction(result):
            return await result
        else:
            return result        
    return _awaitmee
