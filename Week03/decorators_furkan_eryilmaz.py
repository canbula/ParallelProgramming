import time
import tracemalloc

def performance(function_):
    def wrapper(*args, **kwargs):
        if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        start_time = time.time()
        tracemalloc.start()
        result = function_(*args, **kwargs)
        traced_memory = tracemalloc.get_traced_memory()
        if traced_memory:
            performance.total_mem += traced_memory[1]

        tracemalloc.stop()
        end_time = time.time()

        performance.counter += 1
        performance.total_time += end_time - start_time

        return result

    return wrapper
