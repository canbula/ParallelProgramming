import time
import tracemalloc
#docstring için gpt kullandım
# Performans dekoratörü
def performance(func):
    """
      docstring için gpt kullandım
    Bir fonksiyonun zaman ve bellek kullanımını ölçen dekoratör.

    Özellikler:
    ----------
    counter : int
        Dekore edilen fonksiyonun kaç kez çağrıldığını sayar.
    total_time : float
        Fonksiyonun tüm çağrılarda toplam çalışma süresi (saniye cinsinden).
    total_mem : int
        Fonksiyonun tüm çağrılarda en yüksek bellek kullanımını (bayt cinsinden) verir.

    Parametreler:
    ------------
    func : callable
        Performansı ölçülecek olan fonksiyon.

    Döndürür:
    ---------
    callable
        `func` çağrıldığında performansını ölçen bir sarmalayıcı fonksiyon döndürür.
    """
    
    # Performans metriklerini başlat
    performance.counter = 0
    performance.total_time = 0.0
    performance.total_mem = 0.0

    # Sarmalayıcı fonksiyonu tanımla
    def wrapper(*args, **kwargs):
        """
        Çalışma süresini ve bellek kullanımını ölçen sarmalayıcı fonksiyon.

        Parametreler:
        ------------
        *args : tuple
            Dekore edilen fonksiyona iletilecek konumsel argümanlar.
        **kwargs : dict
            Dekore edilen fonksiyona iletilecek anahtar-değer argümanları.

        Döndürür:
        ---------
        result
            Dekore edilen fonksiyonun sonucu.
        """
        
        # Bellek izlemeyi başlat
        tracemalloc.start()
        
        # Zaman ölçümünü başlat
        start_time = time.time()
        
        # Asıl fonksiyonu çağır
        result = func(*args, **kwargs)
        
        # Zaman ölçümünü bitir
        end_time = time.time()
        
        # Mevcut bellek ve en yüksek bellek kullanımını al
        current, peak = tracemalloc.get_traced_memory()
        
        # Bellek izlemeyi durdur
        tracemalloc.stop()

        # Performans metriklerini güncelle
        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak

        return result

    return wrapper
