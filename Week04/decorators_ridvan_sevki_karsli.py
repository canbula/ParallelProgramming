import tracemalloc
import time


class PerformanceTracker:
    def __init__(self, func):
        self.func = func
        self.calls = 0
        self.total_time = 0
        self.total_memory = 0

    def __call__(self, *args, **kwargs):
        tracemalloc.start()

        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.calls += 1
        self.total_time += (end - start)
        self.total_memory += peak

        return result
