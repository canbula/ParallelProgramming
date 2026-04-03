import time
import tracemalloc

def performance(func):
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0.0
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        performance.counter += 1
        performance.total_time += elapsed_time
        performance.total_mem += peak_mem
        
        return result
        
    return wrapper
