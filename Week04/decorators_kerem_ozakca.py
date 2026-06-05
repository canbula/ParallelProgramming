import time
import tracemalloc

def calculate_performance(func):
  def wrapper(*args, **kwargs):
    calculate_performance.counter += 1
    # Following up to memory
    tracemalloc.start()

    # Get the initial time
    initial_time = time.perf_counter()

    # Perform decorated function
    result = func(*args, **kwargs)

    # Get the final time
    final_time = time.perf_counter()
    duration = final_time - initial_time
    calculate_performance.total_time += duration

    current, peak = tracemalloc.get_traced_memory()
    calculate_performance.total_mem += peak
    tracemalloc.stop()

    return result
  return wrapper

calculate_performance.counter = 0
calculate_performance.total_time = 0.
calculate_performance.total_mem = 0.
