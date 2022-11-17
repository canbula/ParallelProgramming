```python

import threading
import os

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

def task3():
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 3: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    t3 = threading.Thread(target=task3, name='t3')

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t2.join()
    
 ```
    
# Question : What could be the output of the code below?

## a)

ID of process running main program: 13720

Main thread name: MainThread

Task 1 assigned to thread: t1

ID of process running task 1: 8424

Task 2 assigned to thread: t2

ID of process running task 2: 8424

Task 3 assigned to thread: t3

ID of process running task 3: 8424

## b)

ID of process running main program: 13720

Main thread name: MainThread

Task 1 assigned to thread: t1

ID of process running task 1: 13720

Task 2 assigned to thread: t2

ID of process running task 2: 13720

Task 3 assigned to thread: t3

ID of process running task 3: 13720

## c)

ID of process running main program: 13720

Main thread name: MainThread

Task 1 assigned to thread: t1

ID of process running task 1: 13720

Task 2 assigned to thread: t2

ID of process running task 2: 13720

Task 3 assigned to thread: t3

ID of process running task 3: 8424

## d)
ID of process running main program: 13720

Main thread name: MainThread

Task 1 assigned to thread: t1

ID of process running task 1: 15004

Task 2 assigned to thread: t2

ID of process running task 2: 17596

Task 3 assigned to thread: t3

ID of process running task 3: 8424
