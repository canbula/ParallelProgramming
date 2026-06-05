import threading
import time
def create_threads(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for i in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
                t.start()
            for t in threads:
                t.join()

        return wrapper
    return decorator
@create_threads(5)
def task():
    print(f"{threading.current_thread().name} is running")
    time.sleep(1)
    print(f"{threading.current_thread().name} finished")
task()
