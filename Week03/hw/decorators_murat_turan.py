
import tracemalloc
from time import perf_counter


def performance(x):
    if not hasattr(performance, "counter"):
         performance.counter = 0
    if not hasattr(performance, "total_time"):
         performance.total_time = 0
    if not hasattr(performance, "total_mem"):
         performance.total_mem = 0

    def _performance(*args, **kwargs):
        performance.counter += 1

        tracemalloc.start()
        firs_time = perf_counter()

        value = x(*args, **kwargs)

        last_time = perf_counter()
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        t_time = last_time - first_time

        performance.total_time += t_time
        performance.total_mem += memory
        return value

    return _performance
