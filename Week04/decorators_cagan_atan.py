import tracemalloc
import time


def performance(func):
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0

    def _wrapper(*args, **kwargs):
        performance.counter += 1
        start_time = time.time()
        tracemalloc.start()
        snapshot1 = tracemalloc.take_snapshot()
        result = func(*args, **kwargs)
        snapshot2 = tracemalloc.take_snapshot()
        tracemalloc.stop()
        end_time = time.time()

        performance.total_time += end_time - start_time
        performance.total_mem += snapshot2.compare_to(snapshot1, "lineno")[0].size_diff

        return result

    return _wrapper
