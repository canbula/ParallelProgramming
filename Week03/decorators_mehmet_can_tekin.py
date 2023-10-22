import time
import tracemalloc

def performance(func):
    def _performance(*args,**kwargs):
        if not hasattr(performance,"counter"):
            performance.counter=0
            performance.total_time=0
            performance.total_mem=0

        tracemalloc.start()
        fn_start=time.perf_counter()
        result=func(*args,**kwargs)
        performance.total_mem+=tracemalloc.get_traced_memory()[1]
        fn_end=time.perf_counter()
        tracemalloc.stop()

        performance.counter+=1
        performance.total_time+=fn_end-fn_start
        return result
    return _performance
