import os
import inspect
import time
import random
import tracemalloc

def performance(func):
    """
    A decorator to measure the performance of a function.

    Attributes:
        counter: How many times the function has been called.
        total_time: The total time the function has taken to run.
        total_mem: The total memory used by the function.
    """

    # Initialize the counters
    performance.counter = 0
    performance.total_time = 0.0
    performance.total_mem = 0.0

    def wrapper(*args, **kwargs):
        # Start tracking memory
        tracemalloc.start()
        
        # Record the start time
        start_time = time.time()
        
        # Call the actual function
        result = func(*args, **kwargs)
        
        # Calculate how long it took
        time_taken = time.time() - start_time
        
        # Capture the peak memory usage
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Update the stats
        performance.counter += 1
        performance.total_time += time_taken
        performance.total_mem += peak_mem  # Peak memory during execution
        
        return result
    
    return wrapper

# Test functions
@performance
def example_function(x):
    time.sleep(x)
    return x ** 2

@performance
def memory_intensive_function(size):
    return [random.randint(0, 100) for _ in range(size)]

# Execute test functions
example_function(1)
example_function(2)
example_function(3)
memory_intensive_function(1000000)

# Access performance metrics
print(f"Function called {performance.counter} times.")
print(f"Total time taken: {performance.total_time:.4f} seconds.")
print(f"Total memory used: {performance.total_mem / 1024:.2f} KB.")
