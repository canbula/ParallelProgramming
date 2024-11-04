import tracemalloc,time


def performance(f):
    """
    This function is a decorator used to measure the performance of a function.

    Attributes:
        counter (int): The number of times the decorated function has been called.
        total_mem (int): The total peak memory usage across all calls to the decorated function.
        total_time (float): The total time taken by all calls to the decorated function in seconds.

    Args:
        f (function): The function to be decorated.

    Returns:
        function: The wrapper function that performs the tracking and calls the original function.

    """
     
    setattr(performance, 'counter', 0)
    setattr(performance, 'total_mem', 0)
    setattr(performance, 'total_time', 0)

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + peak)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + end_time - start_time)
        
        return result

    return wrapper
