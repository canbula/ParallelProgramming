import time
import tracemalloc
def performance(fn):
    if not hasattr(performance,"counter"):
        setattr(performance,"counter",0)    
        setattr(performance,"total_time",0)    
        setattr(performance,"total_mem",0)
    def wrapper(*args,**kwargs):
        tracemalloc.start()
        startT = time.perf_counter()
        result = fn(*args,**kwargs)
        endT = time.perf_counter()
        timeT = endT - startT
        n, high = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        performance.total_time += timeT
        performance.counter += 1
        performance.total_mem += high
        return result
    return wrapper

        
