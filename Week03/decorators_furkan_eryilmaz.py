import time
import sys

def performance(function_):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function_(*args, **kwargs)
        end_time = time.time()

        if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += sys.getsizeof(result)
    return wrapper
