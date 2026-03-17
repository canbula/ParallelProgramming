import time
import tracemalloc
from functools import wraps

def performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Sayaç artır
        performance.counter += 1
        # Zaman ölçümü başlat
        start_time = time.perf_counter()
        # Bellek ölçümü başlat
        tracemalloc.start()
        # Fonksiyonu çalıştır
        result = func(*args, **kwargs)
        # Bellek ölçümü bitir
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Zaman ölçümü bitir
        end_time = time.perf_counter()
        # Toplam süreyi ekle
        performance.total_time += (end_time - start_time)
        # Toplam bellek (peak değer)
        performance.total_mem += peak
        return result
    return wrapper

performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
