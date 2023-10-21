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
        # print(f"start time: {start_time}")
        tracemalloc.start()
        performance.counter += 1
        # print(f"counter: {performance.counter}")
        func(*args, **kwargs)
        end_time = time.perf_counter()
        # print(f"end_time: {end_time}")
        tracemalloc.stop()
        mem_usage = tracemalloc.get_traced_memory()
        performance.total_mem += mem_usage[1]
        # print(f"total memory: {performance.total_mem}")
        performance.total_time += (end_time - start_time)
        # print(f"total time: {performance.total_time}")

    return _performance


@performance
def performance_Test():
    """
    Example function performance_Test for performance measurement.
    This function is an example that demonstrates how to use
    the performance decorator.
    """
    print("----")


performance_Test()
