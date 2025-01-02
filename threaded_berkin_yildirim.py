import threading

def threaded(n):
    """
    Decorator to run a function n times in separate threads.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for i in range(n):
                thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        return wrapper
    return decorator
