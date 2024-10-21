import asyncio

def awaitme(func):
    """
    Bu decorator, senkron fonksiyonları asenkron olarak çalıştırır.
    
    Eğer verilen fonksiyon zaten bir coroutine (asenkron fonksiyon) ise direkt await eder.
    Eğer senkron bir fonksiyon ise, bu fonksiyon mevcut event loop'ta çalıştırılır.
    Event loop yoksa yeni bir loop oluşturur.
    
    :param func: Senkron veya asenkron fonksiyon
    :return: Asenkron fonksiyon olarak döndürür
    """
    async def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, func, *args)
    return wrapper
