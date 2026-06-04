import time
import functools
import tracemalloc

def performance(func):
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TIME
        start_time = time.time()

        # MEMORY
        tracemalloc.start()
        start_mem, _ = tracemalloc.get_traced_memory()

        result = func(*args, **kwargs)

        end_mem, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        end_time = time.time()

        # UPDATE STATS
        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += (end_mem - start_mem)

        return result

    return wrapper
