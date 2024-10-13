import time
import tracemalloc

def performance(func):
    """
    This function with a wrapper is to be used as a decorator.
    Tracks execution time, memory usage, and counts function calls.
    """
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        setattr(wrapper, 'counter', getattr(wrapper, 'counter', 0) + 1)
        setattr(wrapper, 'total_time', getattr(wrapper, 'total_time', 0) + (end - start))
        setattr(wrapper, 'total_mem', getattr(wrapper, 'total_mem', 0) + peak)

        return result

    setattr(wrapper, 'counter', 0)
    setattr(wrapper, 'total_time', 0)
    setattr(wrapper, 'total_mem', 0)

    return wrapper
