import time
import tracemalloc

def performance(function):
    def _performance(*args, **kwargs):
        if not hasattr(performance, "counter"):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        tracemalloc.start()
        start_time = time.perf_counter()
        function(*args, **kwargs)
        end_time = time.perf_counter()
        mem_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += mem_used
        return function
    return _performance
