import threading
import time

def threaded(number_of_threads):
    """
    A decorator that runs a function concurrently using multiple threads.

    :param number_of_threads: The number of threads to spawn to run the decorated function.
    :type number_of_threads: int

    :return: A decorator to wrap a function with threaded execution.
    :rtype: function
    """
    def decorator(func):
        """
        The actual decorator that spawns the threads and runs the function.

        :param func: The function to be executed in multiple threads.
        :type func: function

        :return: The wrapper function that creates threads and runs the decorated function.
        :rtype: function
        """
        def wrapper(*args, **kwargs):
            """
            Wrapper function that creates threads and runs the decorated function.

            :param args: Positional arguments to pass to the decorated function.
            :type args: tuple

            :param kwargs: Keyword arguments to pass to the decorated function.
            :type kwargs: dict
            """
            threads = []
            for i in range(number_of_threads):
                thread = threading.Thread(target=func, args=args, kwargs=kwargs, name=f"Thread-{i}")
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        return wrapper
    return decorator
