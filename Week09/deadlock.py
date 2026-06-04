import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def thread_func1():
    with lock_a:
        print("Thread 1: Holding lock_a...")
        time.sleep(1)
        with lock_b:
            print("Thread 1: Acquired lock_b!")


def thread_func2():
    with lock_b:
        print("Thread 2: Holding lock_b...")
        time.sleep(1)
        with lock_a:
            print("Thread 2: Acquired lock_a!")


t1 = threading.Thread(target=thread_func1)
t2 = threading.Thread(target=thread_func2)

t1.start()
t2.start()

t1.join()
t2.join()
