from time import perf_counter
import tracemalloc

def performance(function_):
    def wrapper(*args, **kwargs):
        if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        tracemalloc.start()
        start_time = perf_counter()
        result = function_(*args, **kwargs)
        traced_memory = tracemalloc.get_traced_memory()
        if traced_memory:
            performance.total_mem += traced_memory[1]

        end_time = perf_counter()
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += end_time - start_time

        return result

    return wrapper
