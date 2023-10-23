import time,tracemalloc
def performance(func):
    def wrapper(*args,**kwargs):
        if not hasattr(performance,'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0
            
        performance.counter +=1
        start = time.perf_counter()
        tracemalloc.start()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        execution_time = start - end
        performance.total_mem = tracemalloc.get_traced_memory()[1]
        performance.total_time = execution_time
        return result

    return  wrapper
