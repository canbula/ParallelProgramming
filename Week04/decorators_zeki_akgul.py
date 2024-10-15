from time import perf_counter
import tracemalloc

def performance(fn):
    if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

    def _performance(*args, **kwargs):
        tracemalloc.start()
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        performance.total_mem += tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        performance.counter += 1
        performance.total_time += end - start
        return result
    return _performance
