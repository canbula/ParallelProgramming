import time
import tracemalloc
def performance(func):
    if not hasattr(performance,"counter"):
        setattr(performance,"counter",0)
    
    if not hasattr(performance,"total_time"):
        setattr(performance,"total_time",0)
    
    if not hasattr(performance,"total_mem"):
        setattr(performance,"total_mem",0)
    
    def _d1(*args,**kwargs):
         tracemalloc.start()
         start_time = time.perf_counter()
         result = func(*args,**kwargs)
         end_time = time.perf_counter()
         elapsed = end_time - start_time
         current_mem, peak_mem = tracemalloc.get_traced_memory()
         performance.counter += 1
         performance.total_time += elapsed
         performance.total_mem += peak_mem
         return result
    return _d1

