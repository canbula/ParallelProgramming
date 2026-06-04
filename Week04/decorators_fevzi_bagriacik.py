import time
import tracemalloc
from functools import wraps

class performance:
    counter = 0
    total_time = 0.0
    total_mem = 0

    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        result = self.func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak

        return result
