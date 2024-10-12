import time
import tracemalloc

def performance(fn):
    """
    Decorator to measure performance metrics of a function.

    This decorator tracks the execution time and memory usage of the decorated
    function, printing the results after each call.

    :param fn: The function to be decorated.
    :returns: A wrapped function that tracks performance metrics.
    :raises Exception: If an error occurs during the execution of the decorated function.
    """

    setattr(performance, 'counter', 0)
    setattr(performance, 'total_time', 0.0)
    setattr(performance, 'total_mem', 0.0)

    def _performance(*args, **kwargs):
        """
        Wrapper function that measures execution time and memory usage.

        :param args: Positional arguments to be passed to the decorated function.
        :param kwargs: Keyword arguments to be passed to the decorated function.
        """
        counter = getattr(performance, 'counter')
        total_time = getattr(performance, 'total_time')
        total_mem = getattr(performance, 'total_mem')

        counter += 1
        setattr(performance, 'counter', counter)

        tracemalloc.start()
        start_time = time.time()

        try:
            fn(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            elapsed_time = end_time - start_time
            memory_usage = peak

            total_time += elapsed_time
            total_mem += memory_usage

            setattr(performance, 'total_time', total_time)
            setattr(performance, 'total_mem', total_mem)

            print_results(fn.__name__, elapsed_time, memory_usage, counter, total_time, total_mem)

    return _performance

def print_results(func_name, elapsed_time, memory_usage, counter, total_time, total_mem):
    """
    Display the performance results of the decorated function.

    This function prints the name of the function being measured, the elapsed time,
    memory usage, and the total statistics over all calls.

    :param func_name: The name of the function being measured.
    :param elapsed_time: The time taken for the function to execute, in seconds.
    :param memory_usage: The peak memory usage during the function execution, in bytes.
    :param counter: Number of times the decorated function has been called.
    :param total_time: Total execution time of the decorated function.
    :param total_mem: Total peak memory usage of the decorated function.
    """
    results = (
        f"Function Name: {func_name}\n"
        f"Number of Calls: {counter}\n"
        f"Elapsed Time: {elapsed_time:.6f} seconds\n"
        f"Memory Usage: {memory_usage / 1024:.2f} KB\n"
        f"Total Time: {total_time:.6f} seconds\n"
        f"Total Memory Usage: {total_mem / 1024:.2f} KB\n"
    )
    print(results)
