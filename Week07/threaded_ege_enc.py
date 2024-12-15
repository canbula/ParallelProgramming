import threading


def threader(n : int):
    """
    This function is a decorator which takes an integer n as an argument
    and returns a threaded function.

    :param n:Number of threads
    :return:Threaded function

    """
    def decorator(func):
        def wrapper():
            threads = []
            for _ in range(n):  # 5 thread oluştur
                t = threading.Thread(target=func)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        return wrapper
    return decorator

@threader(4)
def func():
    print("Hello World")

func()
