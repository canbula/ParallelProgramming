import time
import tracemalloc
import functools


def performance(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        performance.counter += 1

        tracemalloc.start()
        start = time.perf_counter()

        result = fn(*args, **kwargs)

        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.total_time += (end - start)
        performance.total_mem += peak

        return result

    return wrapper


performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0
