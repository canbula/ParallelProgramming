import asyncio

def awaitme(_synchronous_function):
    async def asynchronous_wrapper(*args, **kwargs):
        result = _synchronous_function(*args, **kwargs)
        if asyncio.iscoroutinefunction(_synchronous_function):
            return await result
        return result
    
    return asynchronous_wrapper