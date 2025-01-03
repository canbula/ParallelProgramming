import time
import tracemalloc

def performance(func):
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak

        return result

    return wrapper
