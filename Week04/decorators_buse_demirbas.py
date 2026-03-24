import time
import tracemalloc
 
 
def performance(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        t0 = time.time()
        result = func(*args, **kwargs)
        performance.total_time += time.time() - t0
        performance.total_mem += tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        performance.counter += 1
        return result
    return wrapper
 
performance.counter = 0
performance.total_time = 0
performance.total_mem = 0
 
