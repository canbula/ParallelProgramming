def awaitme(func):
    async def init(*args, **kwargs):
        res = func(*args, **kwargs)
        if hasattr(res, "__await__"):  # eğer await edilebilirse
            return await res
        return res
    return init
