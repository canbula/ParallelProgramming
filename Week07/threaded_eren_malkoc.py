import threading

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for _ in range(n):
                thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()       
        return wrapper
    return decorator
