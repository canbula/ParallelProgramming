import time
import tracemalloc


def performance(func):
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        time1 = time.time()
        result = func(*args, **kwargs)
        time2 = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        performance.counter += 1
        performance.total_time += time2 - time1
        performance.total_mem += peak
        return result
    return wrapper
