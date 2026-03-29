import time
import tracemalloc

def performance(fn):
    counter = 0
    total_time = 0.0
    total_mem = 0

    def wrapper(*args, **kwargs):
        nonlocal counter, total_time, total_mem

        counter += 1

        tracemalloc.start()
        start = time.perf_counter()

        result = fn(*args, **kwargs)

        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time += (end - start)
        total_mem += peak

        return result

    wrapper.get_stats = lambda: (counter, total_time, total_mem)

    return wrapper
