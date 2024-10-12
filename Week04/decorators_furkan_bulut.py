import time
import tracemalloc

class Performance:
    """
    Performance class for measuring execution time and memory usage of functions.

    This class acts as a decorator to track the performance metrics of functions.
    """

    def __init__(self):
        """
        Initialize the Performance class.

        :param counter: Number of times the decorated function has been called.
        :param total_time: Total execution time of the decorated function.
        :param total_mem: Total peak memory usage of the decorated function.
        """
        self.counter = 0
        self.total_time = 0
        self.total_mem = 0

    def __call__(self, func):
        """
        Decorate the given function to measure its performance.

        :param func: The function to be decorated.
        :returns: A wrapped function that tracks performance metrics.
        """
        def _performance(*args, **kwargs):
            self.calculate(func, *args, **kwargs)

        return _performance

    def calculate(self, func, *args, **kwargs):
        """
        Calculate the execution time and memory usage of the decorated function.

        :param func: The function whose performance is to be measured.
        :param args: Positional arguments to be passed to the function.
        :param kwargs: Keyword arguments to be passed to the function.
        :raises Exception: If the function execution fails.
        """
        self.counter += 1
        tracemalloc.start()
        start_time = time.time()

        func(*args, **kwargs)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        elapsed_time = end_time - start_time
        memory_usage = peak

        self.total_time += elapsed_time
        self.total_mem += memory_usage
        self.print_results(func.__name__, elapsed_time, memory_usage)

    def print_results(self, func_name, elapsed_time, memory_usage):
        """
        Display the performance results of the decorated function.

        :param func_name: The name of the function being measured.
        :param elapsed_time: The time taken for the function to execute, in seconds.
        :param memory_usage: The peak memory usage during the function execution, in bytes.
        """
        results = (
            f"Function Name: {func_name}\n"
            f"Number of Calls: {self.counter}\n"
            f"Elapsed Time: {elapsed_time:.6f} seconds\n"
            f"Memory Usage: {memory_usage / 1024:.2f} KB\n"
            f"Total Time: {self.total_time:.6f} seconds\n"
            f"Total Memory Usage: {self.total_mem / 1024:.2f} KB\n"
        )
        print(results)
