import time
import tracemalloc

def performance(fn):
    """A decorator to measure the performance (time and memory usage) of a function."""
    # Static variables for performance tracking
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        # Increment the call counter
        performance.counter += 1

        # Start tracking memory and time
        tracemalloc.start()
        start_time = time.time()

        # Execute the decorated function
        result = fn(*args, **kwargs)

        # Stop tracking memory and calculate elapsed time
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Update total memory and time
        performance.total_mem += peak
        performance.total_time += (end_time - start_time)

        return result

    return wrapper
