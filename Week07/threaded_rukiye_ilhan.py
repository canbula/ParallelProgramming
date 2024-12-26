import threading

def threaded(func):
    def wrapper(n, *args, **kwargs):
        threads = []
        for _ in range(n):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    return wrapper


