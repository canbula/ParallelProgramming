import tracemalloc
import time


def performance_decoraters(func):
    if not hasattr(performance_decoraters ,'counter'):
        performance_decoraters.counter = 0
        performance_decoraters.total_time = 0
        performance_decoraters.total_mem = 0

    def perform(*args,**kwargs):
        tracemalloc.start()  # start to follow memory
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        used_memory = tracemalloc.get_traced_memory()[1]  # [0] gives current memory consumption but [1] gives total(max) memory consumption during thr last fallowing time
        tracemalloc.stop()  # we started memeory following process only to find how much memory uses by thr called function not the entire program ,so we stop memory following when the jop of function is finished
        performance_decoraters.counter += 1
        performance_decoraters.total_time += end_time - start_time
        performance_decoraters.total_mem += used_memory
        return result
    return perform
