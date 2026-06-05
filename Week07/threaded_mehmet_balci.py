import threading

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = [threading.Thread(target=func, args=args, kwargs=kwargs) for _ in range(n)]
            
            for t in threads:
                t.start()
                
            for t in threads:
                t.join()
                
        return wrapper
    return decorator
