import time
import tracemalloc

def performance(func):
    counter = 0
    total_time = 0.0
    total_mem = 0.0

    def wrapped_function(*args, **kwargs):
        nonlocal counter, total_time, total_mem
        
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        counter += 1
        total_time += end_time - start_time
        total_mem += peak_memory

        wrapped_function.counter = counter
        wrapped_function.total_time = total_time
        wrapped_function.total_mem = total_mem

        return result

    wrapped_function.counter = counter
    wrapped_function.total_time = total_time
    wrapped_function.total_mem = total_mem

    return wrapped_function
