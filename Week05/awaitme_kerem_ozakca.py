import asyncio

def convert_to_async_func(func):
  async def wrapper(*args, **kwargs):
    res = func(*args, **kwargs)
    if asyncio.iscoroutine(res):
      return await res
    return res
  return wrapper
