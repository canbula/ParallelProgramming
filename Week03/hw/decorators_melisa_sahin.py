import time
import tracemalloc

def performance(func):
    def wrapper(*args,**kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter()
        memory = tracemalloc.get_traced_memory()[1]
        
        if not hasattr(performance, "counter"):
            performance.counter = 0
        if not hasattr(performance, "total_time"):
            performance.total_time = 0
        if not hasattr(performance, "total_mem"):
            performance.total_mem = 0
        
        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += memory
        
        print(f"Counter: {performance.counter} Total time: {performance.total_time} Total memory: {performance.total_mem}")
        
        return result
    
    return wrapper
