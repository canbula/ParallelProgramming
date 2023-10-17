from time import perf_counter
import tracemalloc

def performance(fn):
    if not hasattr(performance, "counter"):
         performance.counter = 0
    if not hasattr(performance, "total_time"):
         performance.total_time = 0
    if not hasattr(performance, "total_mem"):
         performance.total_mem = 0

    def _fn(*args, **kwargs):
        performance.counter += 1

        tracemalloc.start()
        before_time = perf_counter()

        ret_value = fn(*args, **kwargs)

        after_time = perf_counter()
        max_mem = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        d_time = after_time - before_time

        performance.total_time += d_time
        performance.total_mem += max_mem
        return ret_value

    return _fn

