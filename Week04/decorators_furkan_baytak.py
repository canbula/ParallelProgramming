import time
import sys

def performance(func):

    if not hasattr(performance, 'counter'):
        setattr(performance, 'counter', 0)

    if not hasattr(performance, 'total_time'):
        setattr(performance, 'total_time', 0.0)
    
    if not hasattr(performance, 'total_mem'):
        setattr(performance, 'total_mem', 0)

    def wrapper(*args, **kwargs):
        start_time = time.time()       
        memory_usage=sys.getsizeof(func(*args, **kwargs))
        end_time = time.time()             
            
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + (end_time - start_time))
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + memory_usage)
        
        return func(*args, **kwargs)

    return wrapper

