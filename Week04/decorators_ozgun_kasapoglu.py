import time
import sys
import tracemalloc

tracemalloc.start()


def performance(func):
    def wrapper(*args, **kwargs):
        performance.counter += 1

        tracemalloc.reset_peak()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        performance.total_time += (end_time - start_time)

        _, peak = tracemalloc.get_traced_memory()
        obj_size = sys.getsizeof(result)

        performance.total_mem += max(peak, obj_size)

        return result

    return wrapper


performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0.0
