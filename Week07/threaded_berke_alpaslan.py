import threading

def threaded(n):
    """Creates a decorator that runs the decorated function in multiple threads.

        This decorator creates `n` threads to execute the decorated function concurrently.
        Each thread runs the same function with the same arguments. All threads are started
        and then joined before returning.

        Parameters
        ----------
        n : int
            Number of threads to create and run the function in

        Returns
        -------
        Threaded
            A decorator class that handles the thread creation and management

        Examples
        --------
        >>> @threaded(3)
        ... def example_function(x):
        ...     print(f"Processing {x}")
        ...
        >>> example_function("test")
        Processing test
        Processing test
        Processing test

        Notes
        -----
        - All threads execute the same function with identical arguments
        - The decorator waits for all threads to complete before returning
        - No return values are captured from the threaded function executions

        """
    class Threaded:
        def __init__(self, n):
            self.n = n
        def __call__(self, func):
            def wrapper(*args, **kwargs):
                threads = []
                for i in range(self.n):
                    t = threading.Thread(target=func, args=args, kwargs=kwargs)
                    threads.append(t)
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
            return wrapper
    return Threaded(n)
