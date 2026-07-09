import time
import tracemalloc
import functools
def performance(func):
    """
    A decorator that measures the execution time, memory usage, 
    and call count of the decorated functions.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Increment the global counter for the decorator
        performance.counter += 1
        # Start tracking memory
        tracemalloc.start()
        # Start tracking time
        start_time = time.perf_counter()
        try:
            # Execute the actual function
            result = func(*args, **kwargs)
        finally:
            # Calculate elapsed time
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            # Get memory usage (current, peak)
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            # Stop tracking memory
            tracemalloc.stop()
            # Update global stats
            performance.total_time += elapsed_time
            performance.total_mem += peak_mem
        return result
    return wrapper
# Initialize the static attributes on the function object itself
# This allows all decorated functions to share these counters.
performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
