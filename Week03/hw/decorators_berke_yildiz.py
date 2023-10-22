import tracemalloc,time

def performance(fn):
    if not hasattr(performance,"counter"):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0
    def _performance(*args,**kwargs):
            performance.counter += 1
            start_time = time.time()
            tracemalloc.start()
            fn(*args,**kwargs)
            end_time = time.time()
            performance.total_mem += tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            exec_time = round(end_time - start_time,ndigits=4)
            performance.total_time += exec_time
    return _performance
