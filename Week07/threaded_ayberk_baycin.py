import threading
import random

def threaded_pi_calculator(n):
    """
    n: Thread sayısı.
    Bu decorator, dönen 'hits' listesini otomatik olarak Pi sayısına dönüştürür.
    """
    def decorator(func):
        def wrapper(total_samples, *args, **kwargs):
            # Örnek sayısını thread'lere paylaştır
            samples_per_thread = total_samples // n
            threads = []
            results = []

            def worker():
                # Fonksiyona paylaştırılmış örnek sayısını gönderiyoruz
                res = func(samples_per_thread, *args, **kwargs)
                results.append(res)

            # 1. CREATE & START
            for _ in range(n):
                t = threading.Thread(target=worker)
                threads.append(t)
                t.start()

            # 2. SYNCHRONIZE
            for t in threads:
                t.join()

            # --- HESAPLAMA MANTIĞI ---
            total_hits = sum(results)
            pi_estimate = 4 * total_hits / (samples_per_thread * n)
            return pi_estimate
            
        return wrapper
    return decorator

@threaded_pi_calculator(n=8) # İstediğin thread sayısını buraya yaz
def count_hits(samples):
    """Sadece çember içindeki noktaları sayan saf fonksiyon."""
    hits = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            hits += 1
    return hits

if __name__ == "__main__":  
    target_samples = 1_000_000
    result = count_hits(target_samples)
    print(f"Hesaplanan Pi: {result}")
