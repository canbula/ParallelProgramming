import time
import sys


def performance(func):
    """
    This function is a decorator that measures the performance of a function.
    This decorator function has a nested function called wrapper.
    It measures the time ,memory usage, and how many called of the this function.
    
    :param func: function of the decorator
    :type func: function
    :return: wrapper of the decorator
    :rtype: function
    """
    if not hasattr(performance, 'counter'):
        setattr(performance, 'counter', 0)
    
    if not hasattr(performance, 'total_time'):
        setattr(performance, 'total_time', 0.0)
    
    if not hasattr(performance, 'total_mem'):
        setattr(performance, 'total_mem', 0)

    def wrapper(*args, **kwargs):
        """
        This function is a wrapper that measures the performance of the decorated function.
        It measures the execution time, memory usage, and the number of calls to the function.

        :param *args: Positional arguments to pass to the decorated function.
        :param **kwargs: Keyword arguments to pass to the decorated function.
        :return: The result of the decorated function.
        """
        start_time = time.time()       

        #source https://www.geeksforgeeks.org/find-out-how-much-memory-is-being-used-by-an-object-in-python/
        memory_usage=sys.getsizeof(func(*args, **kwargs))
        end_time = time.time() 
            
            
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + (end_time - start_time))
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + memory_usage)
        
        return func(*args, **kwargs)

    return wrapper


