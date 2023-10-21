import time, tracemalloc

def performance(func):

    if not hasattr(performance, "counter"):
        performance.counter = 0
    if not hasattr(performance, "total_time"):
        performance.total_time = 0
    if not hasattr(performance, "total_mem"):
        performance.total_mem = 0

    def _performance(*args, **kwargs):
        """
        This is a performance measurement decorator.
        :param args: Function arguments
        :param kwargs: Function keyword arguments
        """
        start_time = time.perf_counter()
        tracemalloc.start()
        
        performance.counter += 1
        
        func(*args, **kwargs)
        
        end_time = time.perf_counter()
        tracemalloc.stop()
        mem_usage = tracemalloc.get_traced_memory()
        
        performance.total_mem += mem_usage[1]
        performance.total_time += (end_time - start_time)
        
    return _performance

