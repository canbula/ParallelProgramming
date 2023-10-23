import tracemalloc
from time import perf_counter


def performance(fn):
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0

    def _performance(*args, **kwargs):
        tracemalloc.start()
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        mem_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += end - start
        performance.total_mem += mem_used

        return result
    return _performance
