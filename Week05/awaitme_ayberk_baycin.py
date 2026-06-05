import functools
import asyncio

def awaitme(func):
    """
    Normal bir fonksiyonu coroutine (asenkron fonksiyon) haline getiren decorator.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # Fonksiyonu asenkron bir şekilde çalıştırır ve sonucunu döner
        # loop.run_in_executor veya direkt çağrı yerine coroutine sarmalaması yapılır
        return func(*args, **kwargs)

    return wrapper

# Örnek kullanım:
# @awaitme
# def say_hello(name):
#     return f"Merhaba {name}"

# Bu fonksiyon artık await edilebilir:
# result = asyncio.run(say_hello("Ayberk"))
# print(result)
