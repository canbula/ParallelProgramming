import time
import tracemalloc as tm


def performance(func):
    """
    A decorator function that measures the performance of the given function
    and also saves some statistics.
    (The definition is from the lecture notes.)
    """
    performance.counter = 0
    performance.total_mem = 0.0
    performance.total_time = 0.0

    def _performance(*args, **kwargs):
        tm.start()
        start_time = time.time()

        result = func(*args, **kwargs)

        _, peak_mem = tm.get_traced_memory()
        end_time = time.time()

        tm.stop()

        performance.total_time += end_time - start_time
        performance.total_mem += peak_mem
        performance.counter += 1

        return result

    return _performance
