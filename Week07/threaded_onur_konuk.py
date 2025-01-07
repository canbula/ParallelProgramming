import threading

def threaded(n):
    """
    Decorator to run a function n times in separate threads.

    :param n: Number of threads to create and run the function in
    :type n: int
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for i in range(n):
                thread = threading.Thread(target=func, args=args, kwargs=kwargs, name=f"Thread-{i}")
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        return wrapper
    return decorator
