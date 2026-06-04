import time
import tracemalloc

def performance(fn):
    """Decorator that tracks execution time and memory consumption of a function."""
    # Initialize tracking attributes if not already present
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0
    
    def inner(*args, **kwargs):
        # Update function invocation count
        performance.counter += 1
        
        # Begin memory and execution time monitoring
        tracemalloc.start()
        start = time.time()
        
        # Run the original function
        ret_value = fn(*args, **kwargs)
        
        # End monitoring and capture metrics
        end = time.time()
        current_usage, max_usage = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Accumulate memory and execution time
        performance.total_mem += max_usage
        performance.total_time += (end - start)
        
        return ret_value
    
    return inner
