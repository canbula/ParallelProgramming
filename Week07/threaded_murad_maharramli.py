import threading
from functools import wraps

def threaded(n: int):
    """
    A decorator that executes the wrapped function in 'n' separate threads.
    It handles creating, starting, and synchronizing (joining) the threads.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threads = []
            
            # Create n threads, pointing them to the target function
            for _ in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
            
            # Start all threads
            for t in threads:
                t.start()
            
            # Synchronize the threads by waiting for all of them to finish
            for t in threads:
                t.join()
                
        return wrapper
    return decorator
