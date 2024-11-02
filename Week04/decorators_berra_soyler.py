import time
import tracemalloc

def performance(func):
    """
    A decorator that measures the performance of a function by tracking the 
    number of calls, total execution time, and peak memory usage.

    Attributes:
    - counter: Tracks the number of times the decorated function is called.
    - total_time: Accumulates the total execution time across all calls.
    - total_mem: Accumulates the peak memory usage across all calls.
    """
    setattr(performance, 'counter', 0)
    setattr(performance, 'total_time', 0.0)
    setattr(performance, 'total_mem', 0.0)
    
    def inner(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + (end_time - start_time))
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + peak)
        
        return result
    
    return inner
