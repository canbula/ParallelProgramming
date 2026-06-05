import time
import tracemalloc

def performance(func):
    
    performance.counter = 0
    performance.total_time = 0
    performance.total_mem = 0
    
    def init(*args, **kwargs):
        start_time = time.time()
        tracemalloc.start()
        
        res = func(*args, **kwargs)
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        
        performance.total_time += end_time - start_time
        performance.counter += 1
        performance.total_mem += peak
        
        return res 
    
    return init
