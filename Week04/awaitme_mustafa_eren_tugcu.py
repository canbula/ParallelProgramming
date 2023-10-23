import asyncio

def coroutine(function):
    async def _function(*args, **kwargs):
        """
        This async function is intended to 
        replace the original function it 
        decorates.
        Takes any number of positional and keyword arguments.
        
        """
        
        res = function(*args, **kwargs)
        if asyncio.iscoroutinefunction(function):
            return await res 
        else :
            return res 
    
    return _function 
