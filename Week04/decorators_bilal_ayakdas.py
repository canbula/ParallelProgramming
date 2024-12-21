from time import time
import tracemalloc


def performance(fn):
    if not hasattr(performance, "counter"):
        setattr(performance, "counter", 0)

    if not hasattr(performance, "total_time"):
        setattr(performance, "total_time", 0.0)

    if not hasattr(performance, "total_mem"):
        setattr(performance, "total_mem", 0)

    def calculate_perf(*args, **kwargs):

        tracemalloc.start()
        begin_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        current, peak = tracemalloc.get_traced_memory()

        setattr(performance, "counter", getattr(performance, "counter") + 1)
        setattr(performance, "total_time", getattr(performance, "total_time") + (end_time - begin_time))
        setattr(performance, "total_mem", getattr(performance, "total_mem") + peak)

        return result

    return calculate_perf
