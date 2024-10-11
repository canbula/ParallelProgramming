import time
import psutil

total_time = 0
total_mem = 0
counter = 0

def performance(fn):
    """
    A decorator function to measure the performance of a given function by tracking 
    both its execution time and memory usage. 

    This decorator calculates the time taken for the function to run and the 
    memory used before and after its execution. It also maintains a global counter 
    of how many times the decorated function has been called, along with 
    accumulating the total time and memory usage.

    :param fn: Function to be decorated and monitored.
    :type fn: Callable
    :return: A wrapper function that monitors performance of the original function.
    :rtype: Callable
    
    Global Variables:
    - **total_time** (float): Accumulates the total execution time across all invocations.
    - **total_mem** (int): Accumulates the total memory difference across all invocations.
    - **counter** (int): Tracks how many times the decorated function has been executed.
    
    Example usage::

        @performance
        def my_function():
            pass
        
        my_function()
    """
    def wrapper(*args, **kwargs):
        global total_time, total_mem, counter
        process = psutil.Process()

        mem_before = process.memory_info().rss
        time_before = time.time()

        counter += 1
        fn(*args, **kwargs)

        time_after = time.time()
        total_time += time_after - time_before

        mem_after = process.memory_info().rss
        total_mem += mem_after - mem_before

    return wrapper
