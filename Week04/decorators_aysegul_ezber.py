import time
import tracemalloc

def track_performance(func):
    """
    A decorator that tracks performance metrics of a function, such as
    the number of invocations, total execution time, and peak memory usage.

    Attributes:
    - call_count: Tracks how many times the decorated function is called.
    - total_duration: Accumulates the total execution time for all calls.
    - peak_memory: Accumulates the peak memory usage across all calls.
    """
    setattr(track_performance, 'call_count', 0)
    setattr(track_performance, 'total_duration', 0.0)
    setattr(track_performance, 'peak_memory', 0.0)

    def wrapper(*args, **kwargs):
        memory_tracker.start()  # Start memory tracking
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the original function
        end_time = time.time()  # Record the end time
        current, peak = memory_tracker.get_traced_memory()  # Get memory usage data
        memory_tracker.stop()  # Stop memory tracking

        # Update performance metrics
        setattr(track_performance, 'call_count', getattr(track_performance, 'call_count') + 1)
        setattr(track_performance, 'total_duration', getattr(track_performance, 'total_duration') + (end_time - start_time))
        setattr(track_performance, 'peak_memory', getattr(track_performance, 'peak_memory') + peak)

        return result

    return wrapper

# Example usage
@track_performance
def sample_function(n):
    """
    A simple function that calculates the sum of the first `n` integers.
    """
    total = sum(range(n))
    time.sleep(0.5)  # Simulate a delay
    return total

