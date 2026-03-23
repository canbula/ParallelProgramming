import tracemalloc as tm
from time import time as now


def performance_tracker(fn):
    """
    Decorator that gathers call count, execution time and memory usage.
    """

    performance_tracker.counter = 0
    performance_tracker.total_time = 0.0
    performance_tracker.total_mem = 0.0

    def execute(*args, **kwargs):
        tm.start()

        t1 = now()
        res = fn(*args, **kwargs)
        t2 = now()

        mem_current, mem_peak = tm.get_traced_memory()
        tm.stop()

        performance_tracker.counter += 1
        performance_tracker.total_time += (t2 - t1)
        performance_tracker.total_mem += mem_peak

        return res

    return execute
