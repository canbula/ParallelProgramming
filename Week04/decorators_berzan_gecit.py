import time
import tracemalloc


def performance(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        mem, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        performance.counter += 1
        performance.total_time += t2 - t1
        performance.total_mem += mem
        return res
    return wrapper

performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0
