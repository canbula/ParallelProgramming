
import time
import sys

def performance(func):
    if not hasattr(performance, 'counter'):
        performance.counter = 0
    if not hasattr(performance, 'total_time'):
        performance.total_time = 0
    if not hasattr(performance, 'total_mem'):
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        performance.counter += 1

        start_time = time.time()
        start_mem = sys.getsizeof(func)
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        total_mem = sys.getsizeof(result) - start_mem

        performance.total_time += total_time
        performance.total_mem += total_mem

        return result

    return wrapper
