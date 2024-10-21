import time
import tracemalloc

def performance(fn):
    """
    Decorator to measure performance of a function, including
    execution time and memory usage.

    This decorator tracks:
    - The number of times the function is called.
    - The cumulative time taken by the function.
    - The cumulative peak memory usage.

    :param fn: The function to be wrapped and measured.
    :return: The result of the wrapped function.
    """  
    if not hasattr(performance, 'counter'):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        tracemalloc.start()

        time_before = time.time()

        result = fn(*args, **kwargs)

        time_after = time.time()

        curr_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += (time_after - time_before)  
        performance.total_mem += peak_mem  

        return result

    return wrapper
