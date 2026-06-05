import time

class Timer:
    """
    Bir kod bloğunun çalışma süresini ölçen Context Manager sınıfı.
    """
    def __init__(self):
        # Public öznitelikleri (attributes) tanımla
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        # 'with' bloğuna girildiğinde çalışır
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 'with' bloğundan çıkıldığında çalışır
        self.end_time = time.perf_counter()
        
    @property
    def elapsed_time(self):
        # Toplam süreyi hesaplamak istersen kullanışlı bir ekleme
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None

# Örnek Kullanım:
# with Timer() as t:
#     # Buraya ölçmek istediğin kodları yaz
#     time.sleep(1)
#
# print(f"Başlangıç: {t.start_time}")
# print(f"Bitiş: {t.end_time}")
