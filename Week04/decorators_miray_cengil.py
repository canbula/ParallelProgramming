import time
import sys

def performance(func):
    """
    A decorator to measure the performance of a function.

    Attributes:
        counter: The number of times the function has been called.
        total_time: The total time the function has taken to run.
        total_mem: The total memory used by the function in bytes.
    """

    if not hasattr(performance, 'counter'):
        performance.counter = 0
    if not hasattr(performance, 'total_time'):
        performance.total_time = 0.0
    if not hasattr(performance, 'total_mem'):
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()
        
        # Call the actual function and calculate memory usage
        result = func(*args, **kwargs)
        memory_usage = sys.getsizeof(result)
        
        # Calculate time taken
        time_taken = time.time() - start_time
        
        # Update the statistics
        performance.counter += 1
        performance.total_time += time_taken
        performance.total_mem += memory_usage
        
        return result
    
    return wrapper

# Test functions
@performance
def example_function(x):
    time.sleep(x)
    return x ** 2

@performance
def memory_intensive_function(size):
    return [0] * size

if __name__ == "__main__":
    # Run test functions
    example_function(1)
    example_function(2)
    memory_intensive_function(1000000)
    
    # Display performance metrics
    print(f"Function called {performance.counter} times.")
    print(f"Total time taken: {performance.total_time:.4f} seconds.")
    print(f"Total memory used: {performance.total_mem / 1024:.2f} KB.")
