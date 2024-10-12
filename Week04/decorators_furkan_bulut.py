import time
import tracemalloc

counter = 0
total_time = 0
total_mem = 0

def performance(fn):
    """
    Decorator to measure performance metrics of a function.

    This decorator tracks the execution time and memory usage of the decorated
    function, printing the results after each call.

    :param fn: The function to be decorated.
    :returns: A wrapped function that tracks performance metrics.
    :raises Exception: If an error occurs during the execution of the decorated function.
    """

    def _performance(*args, **kwargs):
        """
        Wrapper function that measures execution time and memory usage.

        :param args: Positional arguments to be passed to the decorated function.
        :param kwargs: Keyword arguments to be passed to the decorated function.
        """
        global counter, total_time, total_mem
        counter += 1
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

    return _performance
