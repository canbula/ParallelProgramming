import time 
import tracemalloc
from time import perf_counter

def performance(fn):
    if not hasattr(performance, "counter"):
         performance.counter = 0
    if not hasattr(performance, "total_time"):
         performance.total_time = 0
    if not hasattr(performance, "total_mem"):
         performance.total_mem = 0
   
  
    def _fn (*args, **kwargs):
      performance.counter += 1

      tracemalloc.start()
      start_time = perf_counter()

      value = fn(*args, **kwargs)

      finish_time = perf_counter()
      max_mem = tracemalloc.get_traced_memory()[1]
      tracemalloc.stop()
      d_time = finish_time - start_time

      performance.total_time += d_time
      performance.total_mem += max_mem
      return value

    return _fn
      
      
