import time
import tracemalloc
from functools import wraps


def performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            _, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            wrapper.counter += 1
            wrapper.total_time += time.perf_counter() - start_time
            wrapper.total_mem += peak_memory

    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0

    return wrapper
