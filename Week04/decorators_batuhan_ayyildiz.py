import time
import sys

def performance(func):
    """
    Decorator that measures the execution performance of a function, 
    including its execution time, memory usage, and call count.
    """
    if not hasattr(performance, 'counter'):
        setattr(performance, 'counter', 0)
    
    if not hasattr(performance, 'total_time'):
        setattr(performance, 'total_time', 0.0)
    
    if not hasattr(performance, 'total_mem'):
        setattr(performance, 'total_mem', 0)

    def wrapper(*args, **kwargs):
        """
        Wrapper function that calculates the performance metrics of the 
        decorated function on each call, including its execution time, 
        memory usage, and the total number of calls.
        """
        start_time = time.time()       

        # Measure memory usage of the result returned by func
        memory_usage = sys.getsizeof(func(*args, **kwargs))
        end_time = time.time() 
            
        # Update performance metrics
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + (end_time - start_time))
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + memory_usage)
        
        return func(*args, **kwargs)

    return wrapper
