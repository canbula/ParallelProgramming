import time
import tracemalloc

def performance(fn):
    def _performance(*args, **kwargs):
        if(not hasattr(performance,"counter")):
            setattr(performance,"counter",0)
            setattr(performance,"total_time",0)
            setattr(performance,"mem",0)
        performance.counter += 1
        tracemalloc.start()
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        current,peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        performance.total_mem = peak
        performance.total_time += end_time-start_time
        return result
    return _performance
