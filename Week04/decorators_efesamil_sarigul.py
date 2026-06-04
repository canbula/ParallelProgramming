import time
import tracemalloc
from functools import wraps

def performance(fn):
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0.0
        performance.total_mem = 0

    @wraps(fn)
    def wrapper(*args, **kwargs):
        performance.counter += 1
        
        tracemalloc.start()
        start_time = time.time()
        
        result = fn(*args, **kwargs)
        
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        performance.total_mem += peak
        performance.total_time += (end_time - start_time)
        
        return result

    return wrapper
