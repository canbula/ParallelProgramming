import time
import tracemalloc

def performance(func):
    # Initialize static variables only once (if they don't exist)
    if not hasattr(performance, "counter"):
        performance.counter = 0          # Number of times the function is called
        performance.total_time = 0.0     # Total execution time
        performance.total_mem = 0        # Total peak memory usage

    def wrapper(*args, **kwargs):
        # Start high-resolution timer
        start = time.perf_counter()

        # Start tracking memory allocations
        tracemalloc.start()

        try:
            # Execute the original function
            return func(*args, **kwargs)
        finally:
            # Calculate elapsed time
            elapsed = time.perf_counter() - start

            # Get memory usage (peak = maximum memory used)
            _, peak = tracemalloc.get_traced_memory()

            # Stop memory tracking
            tracemalloc.stop()

            # Update statistics
            performance.counter += 1
            performance.total_time += elapsed
            performance.total_mem += peak

    # Return the wrapper function instead of the original
    return wrapper
