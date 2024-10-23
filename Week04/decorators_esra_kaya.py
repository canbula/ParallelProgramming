import time
import tracemalloc

class Performance:
    def __init__(self, fn):
        self.fn = fn
        self.counter = 0
        self.total_time = 0
        self.total_mem = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1

        tracemalloc.start()
        start_time = time.time()

        result = self.fn(*args, **kwargs)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.total_mem += peak
        self.total_time += (end_time - start_time)

        return result
