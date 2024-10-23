import asyncio

def awaitme(func):
    """
    This function waits if it receives an async function, otherwise it just calls the function.
    :param func: The function to be called.
    """
    async def await_case(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if asyncio.iscoroutine(result):
            return await result
        else:
            return result

    return await_case
