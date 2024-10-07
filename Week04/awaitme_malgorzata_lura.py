from typing import Callable, Awaitable
import asyncio

async def awaitme(fn: Callable[..., Awaitable]) -> Callable[..., Awaitable]:
    async def fnc(*args, **kwargs):
        return await fn(*args, **kwargs)
    return fnc
