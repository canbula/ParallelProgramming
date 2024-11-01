import tracemalloc
import time

def performance(func):
    """
    Decorator to measure the performance of a function in terms of
    execution time and memory usage.

    Attributes:
        counter (int): Counts the number of times the decorated function has been called.
        total_time (float): Accumulates the total execution time of the function calls.
        total_mem (int): Accumulates the total memory used (in bytes) by the function calls.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function with performance tracking.
    """
    
    # Initialize performance attributes
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0

    def _wrapper(*args, **kwargs):
        """
        Wrapper function that measures and accumulates the performance
        metrics of the decorated function.

        Args:
            *args: Variable length argument list for the decorated function.
            **kwargs: Arbitrary keyword arguments for the decorated function.

        Returns:
            function: The result returned by the decorated function.
        """
        
        performance.counter += 1
        start_time = time.time()
        tracemalloc.start()
        snapshot1 = tracemalloc.take_snapshot()
        
        result = func(*args, **kwargs)

        snapshot2 = tracemalloc.take_snapshot()
        tracemalloc.stop()
        end_time = time.time()
        
        # Calculate the memory difference and accumulate it
        performance.total_time += end_time - start_time
        performance.total_mem += snapshot2.compare_to(snapshot1, "lineno")[0].size_diff

        return result

    return _wrapper