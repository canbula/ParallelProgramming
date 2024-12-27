import threading

def threaded(n):
    """İlk fonksiyon - thread sayısını parametre olarak alır"""
    def wrapper(func):
        """İkinci fonksiyon - thread'leri oluşturur ve yönetir"""
        threads = []
        #istenen n sayıdaki tjread oluşturldu
        for _ in range(n):
            t = threading.Thread(target=func)
            threads.append(t)
            t.start()
        # Bütün thread'lerin bitmesini bekle
        for thread in threads:
            thread.join()
        return func  # Orijinal fonksiyonu döndür  
    return wrapper
