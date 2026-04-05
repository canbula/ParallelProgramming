import time
import tracemalloc
from functools import wraps

def performance(fn):
    """Bir fonksiyonun performansını (zaman ve bellek kullanımı) ölçen dekoratör."""
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Statik değişkenleri wrapper üzerinde tanımlıyoruz ki her fonksiyonun kendi sayacı olsun
        if not hasattr(wrapper, "counter"):
            wrapper.counter = 0
            wrapper.total_time = 0
            wrapper.total_mem = 0

        # Çağrı sayacını artır
        wrapper.counter += 1

        # Bellek ve zaman takibini başlat
        tracemalloc.start()
        start_time = time.perf_counter()

        # Dekore edilen fonksiyonu çalıştır
        result = fn(*args, **kwargs)

        # Zamanı ve bellek kullanımını hesapla, takibi durdur
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Toplam bellek ve zamanı güncelle
        wrapper.total_mem += peak
        wrapper.total_time += (end_time - start_time)

        return result

    return wrapper
