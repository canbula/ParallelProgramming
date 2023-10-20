import tracemalloc  # for memory tracking
import time         # for measuring time

def performance(fn): 
    def wrapped_function(*args, **kwargs):  
        tracemalloc.start()  # Start tracking memory usage
        start_time = time.perf_counter()  # Start measuring the time of the process
        result = fn(*args, **kwargs)  # Call the wrapped function with the given arguments and get the result
        end_time = time.perf_counter()  # Finish measuring the time of the process
        mem_used = tracemalloc.get_traced_memory()[1]  # Get the traced memory usage

        if not hasattr(wrapped_function, 'counter'):
            # If 'counter' attribute doesn't exist in the wrapped function, initialize it along with 'total_time' and 'total_mem'
            wrapped_function.counter = 0
            wrapped_function.total_time = 0
            wrapped_function.total_mem = 0

        wrapped_function.counter += 1  # Increment the counter for each function call
        wrapped_function.total_time += end_time - start_time  # Update the total time with the current function's execution time
        wrapped_function.total_mem += mem_used  # Update the total memory usage with the current function's memory usage
        return result  # Return the result of the wrapped function

    return wrapped_function  # Return the wrapped function as the decorator
