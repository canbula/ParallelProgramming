import time
import tracemalloc

def performance(func):
    
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "counter"):
            wrapper.counter = 0
            wrapper.total_time = 0
            wrapper.total_mem = 0

        tracemalloc.start()
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        time_taken = time.time() - start_time
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        wrapper.counter += 1
        wrapper.total_time += time_taken
        wrapper.total_mem += peak_mem
        
        print(f"'{func.__name__}' was called {wrapper.counter} times.")
        print(f"Total time so far: {wrapper.total_time:.4f} seconds.")
        print(f"Total peak memory used: {wrapper.total_mem / 1024:.2f} KB.\n")
        
        return result

    return wrapper
