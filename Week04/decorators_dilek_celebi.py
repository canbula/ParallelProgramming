from time import time
from sys import getsizeof
from functools import wraps

def performance(fn):
    """
    A decorator to measure the performance of a function.
    It tracks the number of calls, total execution time, and memory usage of the function.
    """

    # Initialize performance tracking variables
    performance.counter = 0
    performance.total_time = 0.0
    performance.total_mem = 0

    @wraps(fn)
    def calculate_perf(*args, **kwargs):
        # Measure execution time
        begin_time = time()
        result = fn(*args, **kwargs)
        end_time = time()

        # Measure memory usage
        memory_usage = getsizeof(result)

        # Update performance metrics
        performance.counter += 1
        performance.total_time += (end_time - begin_time)
        performance.total_mem += memory_usage

        return result

    return calculate_perf
