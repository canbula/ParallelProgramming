import time,tracemalloc
def performance(func):
    def wrapper(*args,**kwargs):
        if not hasattr(performance,'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter +=1
        start = time.time()
        tracemalloc.start()
        func()
        performance.total_mem = tracemalloc.get_traced_memory()[1]
        performance.total_time = time.time()-start

      
    return  wrapper
