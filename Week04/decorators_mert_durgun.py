import time
import tracemalloc

def performance(func):
    call_count = 0
    total_time = 0.0
    total_memory = 0.0

    def wrapped(*args, **kwargs):
        nonlocal call_count, total_time, total_memory
        
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        call_count += 1
        total_time += end_time - start_time
        total_memory += peak_memory

        wrapped_function.call_count = call_count
        wrapped_function.total_time = total_time
        wrapped_function.total_memory = total_memory

        return result

    wrapped_function.call_count = call_count
    wrapped_function.total_time = total_time
    wrapped_function.total_memory = total_memory

    return wrapped_function
