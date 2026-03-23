import time
import tracemalloc

def performance(func):
    if not hasattr(performance, 'counter'):
        performance.counter = 0
        performance.total_time = 0.0
        performance.total_mem = 0.0
    def wrapper(*args, **kwargs):
        # 1. Ölçümleri Başlat
        tracemalloc.start()
        start_time = time.perf_counter()
        
        # 2. Asıl Fonksiyonu Çalıştır
        result = func(*args, **kwargs)
        
        # 3. Ölçümleri Bitir
        end_time = time.perf_counter()
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # 4. İstatistikleri Güncelle
        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak_mem
        
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    
    return wrapper
