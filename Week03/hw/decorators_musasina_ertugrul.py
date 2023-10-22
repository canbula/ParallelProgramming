"""
    Musa Sina ERTUGRUL 200316011

    This homework has been done for understanding
    decorators in Python. It has been published at 
    3 th week of course.
"""

import tracemalloc
from time import perf_counter

def performance(fn):
    """
    A decorator for profiling the performance of a Python function.

    This decorator measures the execution time and memory usage of the decorated function.
    
    Parameters:
    fn (callable): The function to be profiled.

    Returns:
    callable: A wrapped function that profiles the input function and updates performance metrics.
    """
    def inner_performance(*args,**kwargs):

        if not hasattr(performance, "counter"):
            performance.counter = 0

        if not hasattr(performance, "total_time"):
            performance.total_time = 0

        if not hasattr(performance, "total_mem"):
            performance.total_mem = 0

        performance.counter += 1
        current_ts = perf_counter()
        tracemalloc.start()

        fn(*args,**kwargs)
        mem = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        current_ts = perf_counter() - current_ts

        performance.total_time += current_ts
        performance.total_mem += mem

    return inner_performance
