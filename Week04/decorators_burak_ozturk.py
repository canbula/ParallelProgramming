import time
import tracemalloc


def performance(func):
    """
    A decorator to measure the performance of a function.
    Attributes:
        counter: The number of times the function has been called.
        total_time: The total time the function has taken to run.
        total_mem: The total peak memory used by the function in bytes.
    """

    # Initialize attributes if they don't already exist
    if not hasattr(performance, 'counter'):
        performance.counter = 0
    if not hasattr(performance, 'total_time'):
        performance.total_time = 0.0
    if not hasattr(performance, 'total_mem'):
        performance.total_mem = 0

    def wrapper(*args, **kwargs):
        # Increment call counter
        performance.counter += 1

        # Measure execution time and memory usage
        start_time = time.time()
        tracemalloc.start()

        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f"Error: {exc}")
            result = None
        finally:
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Update performance metrics
            time_taken = end_time - start_time
            performance.total_time += time_taken
            performance.total_mem += peak

            # Print stats for the current function call
            print(f"{func.__name__}: Calls={performance.counter}, Time={time_taken:.4f}s, "
                  f"Memory={peak / 1024:.1f}KB, TotalTime={performance.total_time:.4f}s, "
                  f"TotalMem={performance.total_mem / 1024:.1f}KB")

        return result

    return wrapper


@performance
def example_function(x):
    return x * x


@performance
def memory_intensive_function(size):
    return [0] * size


if __name__ == "__main__":
    # Run test functions
    example_function(1)
    example_function(2)
    memory_intensive_function(1000000)

    # Display final performance metrics
    print(f"Function called {performance.counter} times.")
    print(f"Total time taken: {performance.total_time:.4f} seconds.")
    print(f"Total memory used: {performance.total_mem / 1024:.2f} KB.")
