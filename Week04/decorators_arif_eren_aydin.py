import time
import sys
def performance(func):
    performance.counter = 0
    performance.total_mem=0
    performance.total_time=0  
    def wrapper(*args,**kwargs):
        performance.counter+=1
        total_mem =sys.getsizeof(func)
        performance.total_mem += total_mem
        total_time_start = time.time()
        func(*args,**kwargs)
        total_time = time.time()-total_time_start
        performance.total_time += total_time  
    return wrapper
