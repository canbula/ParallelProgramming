import time
import sys

def performance(func):
    # Initialize performance tracking attributes only once
    if not hasattr(performance, 'counter'):
        performance.counter = 0

    if not hasattr(performance, 'total_time'):
        performance.total_time = 0.0

    if not hasattr(performance, 'total_mem'):
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        start_time = time.time()  

        # Call the function once and store the result to avoid multiple executions
        result = func(*args, **kwargs)

        # Measure memory usage and time
        memory_usage = sys.getsizeof(result)
        end_time = time.time()

        # Update performance metrics
        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += memory_usage

        return result

    return wrapper
