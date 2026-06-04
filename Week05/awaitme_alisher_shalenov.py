import asyncio

def awaitme(fn):
    async def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)

        if asyncio.iscoroutine(res):
            res = await res

        return res

    return wrapper
