import tracemalloc,time

def decorator(fn):
    if not hasattr(decorator,"counter"):
            decorator.counter = 0
            decorator.total_time = 0
            decorator.total_mem = 0
    def _decorator(*args,**kwargs):
            decorator.counter += 1
            start_time = time.time()
            tracemalloc.start()
            fn(*args,**kwargs)
            end_time = time.time()
            decorator.total_mem += tracemalloc.get_traced_memory()
            tracemalloc.stop()
            exec_time = round(end_time - start_time,ndigits=4)
            decorator.total_time += exec_time
    return _decorator
