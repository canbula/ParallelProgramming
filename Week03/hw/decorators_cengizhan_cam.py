import time
import tracemalloc

def performance(func):
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0

    def wrapped_function(*args, **kwargs):
        start_time = time.perf_counter()
        performance.counter += 1
        tracemalloc.start()

        result=func(*args, **kwargs)

        end_time = time.perf_counter()
        performance.total_mem += tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        performance.total_time +=(end_time-start_time)
        return result



    return wrapped_function
