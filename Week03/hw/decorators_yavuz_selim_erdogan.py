import time
import tracemalloc


def performance(function):
    def wrapper(*args, **kwargs):
        if not hasattr(performance, "counter"):
            performance.counter = 0
        if not hasattr(performance, "total_time"):
            performance.total_time = 0
        if not hasattr(performance, "total_mem"):
            performance.total_mem = 0

        tracemalloc.start()
        start_time = time.perf_counter()
        start_mem = tracemalloc.get_traced_memory()[1]
        function(*args, **kwargs)
        end_time = time.perf_counter()
        end_mem = tracemalloc.get_traced_memory()[1]

        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += end_mem - start_mem

        return function

    return wrapper
