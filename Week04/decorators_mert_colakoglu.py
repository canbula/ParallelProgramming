import time
import tracemalloc

def performance(func):
    """
    Evaluates the execution time and memory footprint of the function.

    :param func: Function to decorate.
    :type func: callable
    :return: Wrapped function.
    :rtype: callable

    :cvar counter: Number of calls.
    :cvar total_time: Total execution time in seconds.
    :cvar total_mem: Total peak memory in bytes.
    """
    def _performance(*args, **kwargs):
        tracemalloc.start()
        start_tick = time.perf_counter()
        
        output = func(*args, **kwargs)
        
        end_tick = time.perf_counter()
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        performance.counter += 1
        performance.total_time += (end_tick - start_tick)
        performance.total_mem += peak_mem
        
        return output

    return _performance

performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0
