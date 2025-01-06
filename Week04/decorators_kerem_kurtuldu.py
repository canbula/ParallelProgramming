import time
import tracemalloc

def measure_performance(func):
    # Initialize performance counters
    measure_performance.call_count = 0
    measure_performance.total_execution_time = 0.0
    measure_performance.total_peak_memory = 0

    def wrapper(*args, **kwargs):
        """Wrapper to measure performance of the decorated function."""
        # Start timing and memory tracking
        start_time = time.perf_counter()  # More precise than time.time()
        tracemalloc.start()  # Start memory tracking

        # Execute the actual function
        result = func(*args, **kwargs)

        # Measure time and memory usage
        execution_time = time.perf_counter() - start_time
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()  # Stop memory tracking

        # Update cumulative stats
        measure_performance.call_count += 1
        measure_performance.total_execution_time += execution_time
        measure_performance.total_peak_memory += peak_memory

        # Display performance metrics
        print(f"Call #{measure_performance.call_count}:")
        print(f"Execution Time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB\n")

        return result

    return wrapper
