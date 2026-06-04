import time
import tracemalloc

def performance(fn):
    def _performance(*args, **kwargs):  # wraps yok, düz wrapper
        performance.counter += 1

        tracemalloc.start()
        start = time.perf_counter()

        result = fn(*args, **kwargs)

        elapsed = time.perf_counter() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.total_time += elapsed
        performance.total_mem += peak

        return result
    return _performance

performance.counter = 0
performance.total_time = 0
performance.total_mem = 0