import time

class Timer:
    """
    A context manager class to measure the time taken by a block of code.

    Attributes:
        start_time (float): The time when the context block started.
        end_time (float): The time when the context block ended.
    """

    def __enter__(self):
        self.start_time = time.time()  # Zaman ölçümünü başlat
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()  # Zaman ölçümünü sonlandır
        self.elapsed_time = self.end_time - self.start_time  # Geçen süreyi hesapla

if __name__ == "__main__":
    with Timer() as timer:
        for i in range(1000000):
            pass

    print(f"Start time: {timer.start_time}")
    print(f"End time: {timer.end_time}")
    print(f"Elapsed time: {timer.elapsed_time} seconds")
