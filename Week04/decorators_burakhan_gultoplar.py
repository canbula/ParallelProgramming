import time
import tracemalloc

def performance(func):
    def inner(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        
        output = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        current, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        
        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak_memory
        
        return output
    
    return inner


performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0
