import tracemalloc
import time
from functools import wraps


def performance(func):
    """
    Decorator to track function performance and record statistics.

    :param func: Function to decorate.
    :type func: callable
    :return: Wrapped function.
    :rtype: callable

    :cvar counter: Number of calls.
    :cvar total_time: Total execution time in seconds.
    :cvar total_mem: Total peak memory in bytes.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            wrapper.counter += 1
            wrapper.total_time += (end_time - start_time)
            wrapper.total_mem += peak

    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    return wrapper
