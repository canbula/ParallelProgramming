import threading

"""
threaded(n)
============

A decorator to run a function multiple times in parallel threads.

This decorator creates `n` threads to execute the decorated function.
Each thread uses the same arguments and keyword arguments passed to the function.
The main thread waits for all created threads to finish before continuing.

Parameters
----------
n : int
    The number of threads to create for executing the function.

Notes
-----
- The function is executed `n` times, each in a separate thread.
- Thread synchronization is handled using the `join()` method.
"""

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for number in range(n):
                threads.append(threading.Thread(target=func, args=args, kwargs=kwargs))

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()
        return wrapper
    return decorator
