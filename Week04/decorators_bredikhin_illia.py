import tracemalloc as tm
from time import time as now


def performance(fn):
    """
    Decorator that gathers call count, execution time and memory usage.
    """

    performance.counter = 0
    performance.total_time = 0.0
    performance.total_mem = 0.0

    def execute(*args, **kwargs):
        tm.start()

        t1 = now()
        res = fn(*args, **kwargs)
        t2 = now()

        mem_current, mem_peak = tm.get_traced_memory()
        tm.stop()

        performance.counter += 1
        performance.total_time += (t2 - t1)
        performance.total_mem += mem_peak

        return res

    return execute
