from time import perf_counter, sleep
class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
    def __enter__(self):
        self.start_time = perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = perf_counter()
        return False
with Timer() as t:
    sleep(2)

print("Elapsed time:", t.end_time - t.start_time, "seconds")
