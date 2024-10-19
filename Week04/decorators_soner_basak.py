import tracemalloc
import time

def performance(func):
    """
    Decorator to measure the performance of a function.

    Performance Metrics:
    - Counter: Number of times the decorated function is called
    - Total Time: Cumulative execution time of the function
    - Total Memory: Cumulative memory usage difference

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that tracks performance metrics.
    """
    performance.counter = 0  # Number of function calls
    performance.total_time = 0  # Total execution time in seconds
    performance.total_mem = 0  # Total memory difference in bytes

    def _dec(*args, **kwargs):
        """
        Wrapper function that tracks performance metrics.

        Increments the function call counter, measures execution time,
        and tracks memory usage before and after the function call.

        Args:
            *args: Positional arguments for the original function.
            **kwargs: Keyword arguments for the original function.

        Returns:
            The result of the original function.
        """
        performance.counter += 1  # Increment function call count
        
        # Start measuring execution time
        start_time = time.time()
        tracemalloc.start()  # Start tracking memory
        
        # Take a snapshot of memory before the function execution
        snapshot1 = tracemalloc.take_snapshot()  
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Take a snapshot of memory after the function execution
        snapshot2 = tracemalloc.take_snapshot()  
        tracemalloc.stop()  # Stop tracking memory
        
        # Measure execution time
        end_time = time.time()

        # Update total execution time and memory usage
        performance.total_time += end_time - start_time
        performance.total_mem += snapshot2.compare_to(snapshot1, "lineno")[0].size_diff

        return result  # Return the result of the original function

    return _dec  # Return the decorated function
