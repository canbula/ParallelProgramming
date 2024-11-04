import tracemalloc
import time


def performance(func):
    if not hasattr(performance,'counter'):
        performance.counter = 0
        performance.total_time = 0
        performance.total_mem = 0

    def perform(*args,**kwargs):
        tracemalloc.start()  # start to follow memory
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        used_memory = tracemalloc.get_traced_memory()[1]  # [0] gives current memory consumption but [1] gives total(max) memory consumption during thr last fallowing time
        tracemalloc.stop()  # we started memeory following process only to find how much memory uses by thr called function not the entire program ,so we stop memory following when the jop of function is finished
        performance.counter += 1
        performance.total_time += end_time - start_time
        performance.total_mem += used_memory
        return result
    return perform
