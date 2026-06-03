import threading
import time

# 1. Dekoratörün kendisi (Argümanı alan katman)
def run_in_threads(n):
    # 2. Fonksiyonu sarmalayan katman
    def decorator(func):
        # 3. Fonksiyon çağrıldığında çalışan asıl katman
        def wrapper(*args, **kwargs):
            threads = []
            
            # n adet thread oluştur ve başlat
            for i in range(n):
                # Orijinal fonksiyona gelen argümanları (*args, **kwargs) aynen aktarıyoruz
                t = threading.Thread(
                    target=func, 
                    args=args, 
                    kwargs=kwargs, 
                    name=f"{func.__name__}-Thread-{i+1}"
                )
                threads.append(t)
                t.start()
                print(f"[BAŞLATILDI] {t.name} (ID: {t.native_id})")
            
            # Tüm thread'lerin bitmesini bekle (Senkronizasyon)
            for t in threads:
                t.join()
                print(f"[BİTTİ] {t.name} işini tamamladı.")
                
            print(f"\nTüm {n} thread başarıyla senkronize edildi ve tamamlandı.\n")
            
        return wrapper
    return decorator


# --- KULLANIM ÖRNEĞİ ---

# Fonksiyonun 4 farklı thread üzerinde aynı anda çalışmasını istiyoruz
@run_in_threads(n=4)
def selamla(isim, gecikme):
    print(f" -> {threading.current_thread().name}: Merhaba {isim}!")
    time.sleep(gecikme)
    print(f" -> {threading.current_thread().name}: Hoşça kal {isim}!")

if __name__ == "__main__":
    print("Ana program başladı.")
    
    # Dekoratörlü fonksiyonu çağırıyoruz
    selamla("Ahmet", gecikme=2)
    
    print("Ana program bitti (Tüm threadler katıldığı/join edildiği için bu satır en son basılır).")
