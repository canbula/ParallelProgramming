import time
import tracemalloc


def performance(function):
    def _performance(*args, **kwargs):
        if not hasattr(performance, "counter"):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1

        started_time = time.perf_counter()

        tracemalloc.start()

        function_result = function(*args, **kwargs)

        ended_time = time.perf_counter()

        execution_time = ended_time - started_time

        performance.total_time += execution_time
        performance.total_mem += tracemalloc.get_traced_memory()[1]

        return function_result

    return _performance

