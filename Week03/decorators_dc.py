from typing import Callable
import time
import random
import tracemalloc


def performance(func: Callable) -> Callable:
    if not hasattr(performance, 'counter'):
        performance.counter = 0
    if not hasattr(performance, 'total_time'):
        performance.total_time = 0
    if not hasattr(performance, 'total_mem'):
        performance.total_mem = 0
    def _performance(*args, **kwargs):
        start = time.perf_counter()
        tracemalloc.start()
        func(*args, **kwargs)
        max_mem = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        end = time.perf_counter()
        performance.counter += 1
        performance.total_time += (end - start)
        performance.total_mem += max_mem
    return _performance

@performance
def just_wait(time_to_wait: int) -> None:
    time.sleep(time_to_wait)

@performance
def random_list(length: int = 10, min_value: int = 0, max_value: int = 100) -> list:
    return [random.randint(min_value, max_value) for _ in range(length)]
