import time
import tracemalloc

def performance(function):
    """
    A decorator to measure the performance of a function.

    Tracks:
    - `counter`: Number of times the function is called.
    - `total_time`: Total execution time in seconds.
    - `total_mem`: Total peak memory usage in bytes (via `tracemalloc`).

    Args:
        function (callable): The function to be measured.

    Returns:
        callable: The wrapped function with performance tracking.
    """
    if not hasattr(performance, 'counter'):
        setattr(performance, 'counter', 0)

    if not hasattr(performance, 'total_time'):
        setattr(performance, 'total_time', 0.0)

    if not hasattr(performance, 'total_mem'):
        setattr(performance, 'total_mem', 0.0)

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + elapsed_time)
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + peak)
        return result

    return wrapper
