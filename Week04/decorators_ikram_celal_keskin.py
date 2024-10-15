import time
import psutil
import os

pid = -1

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
        setattr(performance, 'total_mem', 0.0)

    def wrapper(*args, **kwargs):
        """
        This function is a wrapper that measures the performance of the decorated function.
        It measures the execution time, memory usage, and the number of calls to the function.

        :param *args: Positional arguments to pass to the decorated function.
        :param **kwargs: Keyword arguments to pass to the decorated function.
        :return: The result of the decorated function.
        """
       
        global pid
        start_time = time.time()
        
        if pid == -1:
            pid = os.getpid()
        
        # Get memory usage before the function call
        mem_begin = psutil.Process(pid).memory_info().rss
        try:
            result = func(*args, **kwargs)  # Calling actual function for testing the time and memory
        finally:
            mem_end = psutil.Process(pid).memory_info().rss # Get memory usage after the function call
            
            end_time = time.time() # Get the end time 
            
            setattr(performance, 'counter', getattr(performance, 'counter') + 1)
            setattr(performance, 'total_time', getattr(performance, 'total_time') + (end_time - start_time))
            setattr(performance, 'total_mem', getattr(performance, 'total_mem') + (mem_end - mem_begin))
        
        return result

    return wrapper
