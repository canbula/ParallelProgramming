import time
import sys
from functools import wraps


def performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += sys.getsizeof(result)

        if isinstance(result, list):
            performance.total_mem += sys.getsizeof(result)

            for item in result:
                performance.total_mem += sys.getsizeof(item)

        return result

    return wrapper


performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
