import time
import tracemalloc

def performance(func):
    def wrapper(*args, **kwargs):
        # Sayaç artır
        performance.counter += 1        
        # Bellek ölçümü başlat
        tracemalloc.start()
        # Zaman ölçümü başlat
        start_time = time.perf_counter()       
        # Fonksiyonu çalıştır
        result = func(*args, **kwargs)        
        # Zaman ölçümü bitir
        end_time = time.perf_counter()
        # Bellek ölçümü bitir (peak ve current değerleri al)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()  
        # Toplam süreyi ve belleği ekle
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
