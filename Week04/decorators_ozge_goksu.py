import time
import tracemalloc


def performance(func):
    setattr(performance, 'counter', 0)
    setattr(performance, 'total_time', 0.0)
    setattr(performance, 'total_mem', 0.0)

    def inner(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()  
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + (end_time - start_time))
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + peak)

        return result  

    inner.get_stats = lambda: {
        'counter': getattr(performance, 'counter'),
        'total_time': getattr(performance, 'total_time'),
        'total_mem': getattr(performance, 'total_mem'),
    }

    return inner
