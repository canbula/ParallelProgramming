import time
import tracemalloc

def performance(func):
    """
    A decorator to keep track of how often a function is called,
    how long it takes to run, and how much memory it uses.
    
    Attributes:
        counter: How many times the function has been called.
        total_time: The total time the function has taken to run.
        total_mem: The total memory used by the function.
    """
    
    # Initialize the counters
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0
    
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
        
        # Friendly output
        print(f"'{func.__name__}' was called {performance.counter} times.")
        print(f"Total time so far: {performance.total_time:.4f} seconds.")
        print(f"Total memory used: {performance.total_mem / 1024:.2f} KB.\n")
        
        return result
    
    return wrapper
