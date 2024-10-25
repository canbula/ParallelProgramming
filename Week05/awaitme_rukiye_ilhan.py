import asyncio


def decorator(func):
    async def wrapper(*args,**kwargs):
        rslt = func(*args,**kwargs)
        if asyncio.iscoroutine(rslt):
            return await rslt
        return rslt
    return wrapper
