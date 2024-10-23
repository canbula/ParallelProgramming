import time
import tracemalloc

class PerformanceTracker:
    """
    A decorator class that tracks the performance of a function.
    Attributes:
        counter (int): Number of times the decorated function is called.
        total_time (float): Total time the function has taken.
        total_mem (int): Total memory the function has consumed in bytes.
    """
    def __init__(self, func):
        self.func = func
        self.counter = 0
        self.total_time = 0
        self.total_mem = 0

    def __call__(self, *args, **kwargs):
        """Measures the execution time and memory usage of the function."""
        self.counter += 1

        # Start time measurement
        start_time = time.perf_counter()

        # Start memory tracking
        tracemalloc.start()

        result = self.func(*args, **kwargs)

        # Stop memory tracking
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Stop time measurement
        end_time = time.perf_counter()

        # Update total time and memory
        self.total_time += (end_time - start_time)
        self.total_mem += peak

        # Output statistics (optional for debugging)
        print(f"Function '{self.func.__name__}' called {self.counter} times")
        print(f"Total time taken: {self.total_time:.4f} seconds")
        print(f"Total memory used: {self.total_mem / 1024:.4f} KB")
        
        return result

def performance(func):
    """A simple function decorator to track performance."""
    return PerformanceTracker(func)

# Example function to test
@performance
def compute_squares(n):
    """Returns a list of squared numbers up to n."""
    return [i**2 for i in range(n)]

# Running the decorated function multiple times
if __name__ == "__main__":
compute_squares(1000)
compute_squares(2000)
compute_squares(3000)
