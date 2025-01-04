import threading

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            thread_list = []
            for _ in range(n):
                thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                thread.start()
                thread_list.append(thread)
                
            for _ in thread_list:
                _.join()
            return
        return wrapper
    return decorator
