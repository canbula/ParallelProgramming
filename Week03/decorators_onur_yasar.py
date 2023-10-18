import tracemalloc
import time

def performance(fn):
    def decorator(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        fn(*args, **kwargs)
        end_time = time.perf_counter()
        mem_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += mem_used
    return decorator