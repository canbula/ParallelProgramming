import time
import tracemalloc
from functools import wraps

class PerformanceDecorator:
    # Attributes to store statistics
    counter = 0          # Stores how many times the decorated function is called
    total_time = 0       # Stores the total execution time of all calls
    total_mem = 0        # Stores the total memory consumed by all calls

    @staticmethod
    def measure_performance(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Start measuring time
            start_time = time.time()
            
            # Start measuring memory usage
            tracemalloc.start()
            
            # Execute the actual function
            result = func(*args, **kwargs)
            
            # Stop measuring time
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Get memory usage data
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Update statistics
            PerformanceDecorator.counter += 1
            PerformanceDecorator.total_time += elapsed_time
            PerformanceDecorator.total_mem += peak_mem

            # Print performance data for each function call
            print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds and used {peak_mem} bytes of memory.")
            
            return result
        
        return wrapper

# Example function to test the decorator
@PerformanceDecorator.measure_performance
def example_function(n):
    return sum(i ** 2 for i in range(n))

# Test the decorator by calling the example function multiple times
example_function(10000)
example_function(20000)

# Print out the collected statistics
print(f"Total calls: {PerformanceDecorator.counter}")
print(f"Total execution time: {PerformanceDecorator.total_time:.4f} seconds")
print(f"Total memory used: {PerformanceDecorator.total_mem} bytes")
