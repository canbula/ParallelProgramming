import time
import tracemalloc

def performance_decorator(func):
    """
    A decorator to measure the performance of the decorated function.
    It tracks the execution time and memory usage and stores statistics.
    """
    # Initialize performance attributes for the decorator
    def init_performance_attrs():
        setattr(func, 'counter', 0)          # Count the number of times the function is called
        setattr(func, 'total_time', 0.0)      # Total execution time
        setattr(func, 'total_mem', 0.0)       # Total memory used

    # Initialize performance tracking for the first time
    if not hasattr(func, 'counter'):
        init_performance_attrs()

    def wrapper(*args, **kwargs):
        # Access the current performance attributes
        counter = getattr(func, 'counter')
        total_time = getattr(func, 'total_time')
        total_mem = getattr(func, 'total_mem')

        # Start memory tracking
        tracemalloc.start()
        
        # Start the timer to measure execution time
        start_time = time.time()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
        except Exception as e:
            # Handle any exceptions raised during function execution
            print(f"Error occurred while executing {func.__name__}: {e}")
            result = None
        finally:
            # End the timer and stop memory tracking
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Calculate time taken and memory used
            elapsed_time = end_time - start_time
            memory_usage = peak

            # Update performance statistics
            counter += 1
            total_time += elapsed_time
            total_mem += memory_usage

            # Save updated statistics back to the function attributes
            setattr(func, 'counter', counter)
            setattr(func, 'total_time', total_time)
            setattr(func, 'total_mem', total_mem)

            # Print performance results
            print(f"Function '{func.__name__}' executed.")
            print(f"Execution time: {elapsed_time:.6f} seconds")
            print(f"Memory usage: {memory_usage / 1024:.2f} KB")
            print(f"Total calls: {counter}")
            print(f"Total time: {total_time:.6f} seconds")
            print(f"Total memory used: {total_mem / 1024:.2f} KB")

        return result

    return wrapper

# Example usage of the decorator

@performance_decorator
def example_function(n):
    """
    A simple function that simulates some work by sleeping.
    The function calculates the sum of numbers up to n and returns it.
    """
    total = sum(range(n))
    time.sleep(0.5)  # Simulate some work
    return total

# Calling the decorated function
example_function(1000)
example_function(5000)
example_function(10000)
