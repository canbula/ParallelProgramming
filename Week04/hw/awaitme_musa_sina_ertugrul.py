""" Musa Sina ERTUĞRUL 200316011"""

import asyncio

def awaitme(func,*args,**kwargs):
    async def inner_awaitme(*args,**kwargs):
        result = func(*args,**kwargs)
        if asyncio.iscoroutinefunction(func):
            return await result
        else:
            return result
    return inner_awaitme