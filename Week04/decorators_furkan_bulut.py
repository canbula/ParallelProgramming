import time
import tracemalloc


def performance(func):
    """
    A decorator to measure the performance of a function in terms of
    execution time and memory usage.

    This decorator wraps the specified function to track how long it
    takes to execute and how much memory it uses during execution.
    It prints these metrics after the function completes.

    :param func: The function to be decorated.
    :returns: The wrapped function that measures performance.
    """

    func.counter = 0
    func.total_time = 0
    func.total_mem = 0

    def _performance(*args, **kwargs):
        """
        Internal function that executes the decorated function and
        collects performance metrics.

        :param args: Positional arguments to pass to the decorated function.
        :param kwargs: Keyword arguments to pass to the decorated function.
        """

        func.counter += 1  
        tracemalloc.start() 
        start_time = time.time()  

        try:
            result = func(*args, **kwargs)  
        except Exception as e:
            print(f"Error occurred: {e}")
            result = None  
        finally:
            end_time = time.time()  
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()  

            elapsed_time = end_time - start_time 
            memory_usage = peak 

            func.total_time += elapsed_time
            func.total_mem += memory_usage

            print_results(func.__name__, elapsed_time, memory_usage, func.counter, func.total_time, func.total_mem)

        return result  

    return _performance


def print_results(func_name, elapsed_time, memory_usage, counter, total_time, total_mem):
    """
    Print the performance results of the executed function.

    This function formats and outputs the performance metrics,
    including the elapsed time, memory usage, number of calls,
    and total time and memory usage for the decorated function.

    :param func_name: The name of the function whose performance is measured.
    :param elapsed_time: Time taken for the function to execute.
    :param memory_usage: Peak memory usage during the function's execution.
    :param counter: The number of times the function has been called.
    :param total_time: Total time accumulated for all calls.
    :param total_mem: Total memory usage accumulated for all calls.
    """

    results = (
        f"Function Name: {func_name}\n"
        f"Number of Calls: {counter}\n"
        f"Elapsed Time: {elapsed_time:.6f} seconds\n"
        f"Memory Usage: {memory_usage} bytes\n"
        f"Total Time: {total_time:.6f} seconds\n"
        f"Total Memory Usage: {total_mem} bytes\n"
    )
    print(results)
