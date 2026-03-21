import time
import tracemalloc
import functools

def performance(func):
    @functools.wraps(func) # Preserve metadata of the original function
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
        finally:
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            end_time = time.time()
            
            performance.counter += 1
            performance.total_time += (end_time - start_time)
            performance.total_mem += peak
            
        return result
    return wrapper

performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
