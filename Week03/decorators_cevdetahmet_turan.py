import tracemalloc
import time

#print(dir(tracemalloc))

def performance(fn): 
    def wrapped_function(*args, **kwargs):  
        tracemalloc.start()  
        start_time = time.perf_counter()  
        result = fn(*args, **kwargs)  
        end_time = time.perf_counter()  
        mem_used = tracemalloc.get_traced_memory()[1]  

        if not hasattr(performance, 'counter'):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1  
        performance.total_time += end_time - start_time  
        performance.total_mem += mem_used  
        return result 

    return wrapped_function  

# Sample function decorated with 'performance'
@performance
def example_function(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

result = example_function(1000000)

print("Function Calls:", performance.counter)
print("Total Time:", performance.total_time, "seconds")
print("Total Memory:", performance.total_mem, "bytes")
