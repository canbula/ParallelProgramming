import time
import tracemalloc

class PerformanceDecorator:
    def __init__(self, func):
        self.func = func
        self.counter = 0
        self.total_time = 0
        self.total_mem = 0

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        tracemalloc.start()

        result = self.func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        self.counter += 1
        self.total_time += (end_time - start_time)
        self.total_mem += peak

        return result

    def stats(self):
        return {
            'counter': self.counter,
            'total_time': self.total_time,
            'total_mem': self.total_mem
        }

@PerformanceDecorator
def example_function(x, y):
    return x ** y
