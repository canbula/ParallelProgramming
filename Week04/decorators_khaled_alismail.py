import time
import tracemalloc
from functools import update_wrapper


class performance:
    def __init__(self, func):
        self.func = func
        self.counter = 0
        self.total_time = 0.0
        self.total_mem = 0
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        try:
            return self.func(*args, **kwargs)
        finally:
            _, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            self.counter += 1
            self.total_time += time.perf_counter() - start_time
            self.total_mem += peak_memory
