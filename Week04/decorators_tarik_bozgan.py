import time
import tracemalloc

def performance(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        t1 = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        t2 = time.perf_counter()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Hata buradaydı: Sayaçları wrapper'a değil, performance fonksiyonuna ekliyoruz
        performance.counter += 1
        performance.total_time += (t2 - t1)
        performance.total_mem += peak
        
        return result
    return wrapper

# Testin beklediği özellikler (Attributes) ana fonksiyona atanmalı
performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
