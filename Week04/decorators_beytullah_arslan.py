import time
import tracemalloc

def performance(func):
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
        wrapper.counter += 1
        wrapper.total_time += (end_time - start_time)
        wrapper.total_mem += peak_mem
        
        return result
    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
   
    
    return wrapper
