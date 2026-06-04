import time
import tracemalloc
from functools import wraps

def performance(func):
    """
    A decorator that measures the performance of functions and saves statistics.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        performance.counter += 1
        
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        _, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak_mem
        
        return result

    return wrapper

# Initialize the required tracking attributes on the decorator
performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0
