import threading
import time

def threaded(number_of_threads):
    class Threaded:
        """
        A class that acts as a decorator to run a function concurrently using multiple threads.

        :param number_of_threads: The number of threads to spawn to run the decorated function.
        :type number_of_threads: int
        """
        def __init__(self, number_of_threads):
            """
            Initializes the Threaded class with the specified number of threads.

            :param number_of_threads: Number of threads to use for the decorated function.
            :type number_of_threads: int
            """
            self.number_of_threads = number_of_threads

        def __call__(self, func):
            """
            Makes the class instance callable and acts as a decorator for the provided function.

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

                for i in range(self.number_of_threads):
                    thread = threading.Thread(target=func, args=args, kwargs=kwargs, name=f"Thread-{i}")
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

            return wrapper

    return Threaded(number_of_threads)
