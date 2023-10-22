import time
import sys

def performance(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'counter'):
            wrapper.counter = 0
            wrapper.total_time = 0
            wrapper.total_mem = 0

        wrapper.counter += 1

        start_time = time.time()
        start_mem = sys.getsizeof(func)
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        total_mem = sys.getsizeof(result) - start_mem

        wrapper.total_time += total_time
        wrapper.total_mem += total_mem



        return result
    return wrapper

