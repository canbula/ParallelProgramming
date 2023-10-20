import time,tracemalloc
def performance(func):
    def wrapper():
        if not hasattr(wrapper,'counter'):
            wrapper.counter = 1
            wrapper.total_time = 0
            wrapper.total_mem = 0
        start = time.time()
        tracemalloc.start()
        func()
        wrapper.total_mem = tracemalloc.get_traced_memory()[1]
        wrapper.total_time = time.time()-start
   
    return  wrapper
