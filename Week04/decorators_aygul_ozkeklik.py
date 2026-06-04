import time
import tracemalloc

def performance(fn):
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0

    def wrapper(*args, **kwargs):
        performance.counter += 1

        start = time.time()
        tracemalloc.start()
        result = fn(*args, **kwargs)
        end = time.time()

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.total_time += (end - start)
        performance.total_mem += peak

        return result

    return wrapper
