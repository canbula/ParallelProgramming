import time
import tracemalloc

def performance(func):
    
    def wrapped_function(*args, **kwargs):
        
        wrapped_function.counter += 1
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        wrapped_function.total_time += (end_time - start_time)
        wrapped_function.total_mem += peak_memory

        return result

    wrapped_function.counter = 0
    wrapped_function.total_time = 0.0
    wrapped_function.total_mem = 0.0

    return wrapped_function
