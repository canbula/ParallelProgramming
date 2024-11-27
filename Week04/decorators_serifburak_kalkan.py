import time
import tracemalloc

def performance(func):
    setattr(performance, 'counter', 0)
    setattr(performance, 'total_time', 0)
    setattr(performance, 'total_mem', 0)

    def wrapper(*args, **kwargs):
        setattr(performance, 'counter', performance.counter + 1)

        start_time = time.time()
        tracemalloc.start()
        start_mem = tracemalloc.get_traced_memory()[1]
        result = func(*args, **kwargs)

        end_time = time.time()
        end_mem = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        setattr(performance, 'total_time', performance.total_time + (end_time - start_time))
        setattr(performance, 'total_mem', performance.total_mem + (end_mem - start_mem))

        return result

    return wrapper
