import time
import tracemalloc

def performance(func):
    """
    This function with a wrapper is to be used as a decorator.
    Tracks execution time, memory usage, and counts function calls.
    """
    wrapper.counter = 0
    wrapper.total_time = 0
    wrapper.total_mem = 0

    def wrapper(*args, **kwargs):
        tracemalloc.start()

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        wrapper.counter += 1
        wrapper.total_time += end - start
        wrapper.total_mem += peak

        return result

    return wrapper
