def awaitme(func):
   async def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
   return wrapper
