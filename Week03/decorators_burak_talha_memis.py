import time
import tracemalloc

def decorator(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter() 
        func(*args, **kwargs)
        end_time = time.perf_counter()
        mem_used = tracemalloc.get_traced_memory()[1] 

        if not hasattr(decorator, 'counter'):
            decorator.counter = 0
        if not hasattr(decorator, 'total_time'):
            decorator.total_time = 0
        if not hasattr(decorator, 'total_mem'):
            decorator.total_mem = 0

        decorator.counter += 1
        decorator.total_time += end_time - start_time
        decorator.total_mem += mem_used 

        print(f"counter = {decorator.counter}, Total time = {decorator.total_time}, Total mem = {decorator.total_mem}")
        return func
    return wrapper
'''
@decorator
def example_function():
    print("Deneme")
example_function() 
example_function()  
''' 
