import time
import tracemalloc

def performance(func):
    
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        _, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        wrapper.total_time += (end_time - start_time)
        wrapper.total_mem += peak_mem
        
        return result
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    
    if hasattr(func, '__annotations__'):
        wrapper.__annotations__ = func.__annotations__
    
    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    
    return wrapper
