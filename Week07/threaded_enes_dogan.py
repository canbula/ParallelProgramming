import threading
def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for i in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
                t.start()
            for thread in threads:
                thread.join()
        return wrapper
    return decorator