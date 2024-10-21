import time
import tracemalloc
from functools import wraps

def performance(func):
  """
  Decorator that measures the performances of a function by tracking the function by tracking the following:
  - Number of times the function has been called (counter)
  - Total time the function took (total_time)
  - Total memory consumed by the function in bytes (total_mem)

  Attributes:
  -----------
  counter : int
    Stores the number of times the decorated function has been called.
  total_time : float
    Stores the total execution time of all function calls.
  total_mem : int
    Stores the total memory consumed in bytes across all calls.
    """
  performance.counter = 0
  performance.total_time = 0.0
  performance.total_mem = 0

  @wraps(func)
  def wrapper(*args, **kwargs):
    performance.counter += 1

    start_time = time.perf_counter()
    tracemalloc.start()

    result = func(*args,**kwargs)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    performance.total_time += (end_time - start_time)
    performance.total_mem += peak

    return result
  return wrapper

def sample_function(n):
  """
  A sample function that performs some operations to demonstrate the performance decorator.
  """
  return sum([i**2 for i in range(n)])

sample_function(10000)
sample_function(20000)

print(f"Function called: {performance.counter} times")
print(f"Total time: {performance.total_time:.4f} seconds")
print(f"Total memory used: {performance.total_mem} bytes")
