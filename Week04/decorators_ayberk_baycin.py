import time
import functools
import os
import psutil  

def performance(func):
    """
    Fonksiyonun performansını ölçen ve istatistiklerini tutan decorator.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # İşlem başlamadan önceki zaman ve bellek
        start_time = time.perf_counter()
        process = psutil.Process(os.getpid())
        start_mem = process.memory_info().rss
        
        # Fonksiyonu çalıştır
        result = func(*args, **kwargs)
        
        # İşlem bittikten sonraki zaman ve bellek
        end_time = time.perf_counter()
        end_mem = process.memory_info().rss
        
        # İstatistikleri güncelle
        wrapper.counter += 1
        wrapper.total_time += (end_time - start_time)
        # Sadece pozitif tüketimi (farkı) ekleme
        mem_diff = end_mem - start_mem
        if mem_diff > 0:
            wrapper.total_mem += mem_diff
            
        return result

    # İstenen öznitelikleri (attributes) tanımla ve sıfırla
    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    
    return wrapper

# Örnek Kullanım:
@performance
def test_func():
    time.sleep(0.1)
    return [i for i in range(100000)]
