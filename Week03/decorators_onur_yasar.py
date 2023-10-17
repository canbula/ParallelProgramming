import time
import psutil
import os

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def performance(fn):
    def decorator(*args, **kwargs):
        mem_before = process_memory()
        start_time = time.time()
        fn(*args, **kwargs)
        end_time = time.time()
        mem_after = process_memory()

        if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += mem_after - mem_before
    return decorator
