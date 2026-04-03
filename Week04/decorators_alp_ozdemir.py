import time
import tracemalloc

def performance(func):
    
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0
    
    def init(*args,**kwargs):
        start_time = time.time()
        tracemalloc.start()
        res = func(*args,**kwargs)
        end_time = time.time()
        n, high = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        performance.total_time += end_time - start_time
        performance.counter += 1
        performance.total_mem += high
        return res 
    return init
