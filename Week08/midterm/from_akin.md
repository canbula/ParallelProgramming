```python 
    
import threading
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def print_range(start_num, end_num) -> None:
    for i in range(start_num, end_num):
        if threading.current_thread().daemon:
            # This daemon thread should monitor if all the threads running this are finished
            logging.info(f"Current active threads: {threading.active_count()}")
            if threading.active_count() == 1:
                logging.info('All threads finished.')
                break
            sleep(1)
        else:
            logging.info(i)
            sleep(0.2)

t1 = threading.Thread(target=print_range, args=(1, 10))
t2 = threading.Thread(target=print_range, args=(-10, 0))
t3 = threading.Thread(target=print_range, args=(0, 1000), daemon=True)


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

if not t1.is_alive() and not t2.is_alive():
      print('Finished')
```

# Which one of the answers below is a possible output of the Python code above?


# a)
```
Thread-1 (print_range): 1
Thread-2 (print_range): -10
Thread-3 (print_range): Current active threads: 4
Thread-2 (print_range): -9
Thread-1 (print_range): 2
Thread-2 (print_range): -8
Thread-1 (print_range): 3
Thread-2 (print_range): -7
Thread-1 (print_range): 4
Thread-2 (print_range): -6
Thread-1 (print_range): 5
Thread-3 (print_range): Current active threads: 4
Thread-1 (print_range): 6
Thread-2 (print_range): -5
Thread-1 (print_range): 7
Thread-2 (print_range): -4
Thread-1 (print_range): 8
Thread-2 (print_range): -3
Thread-2 (print_range): -2
Thread-1 (print_range): 9
Thread-2 (print_range): -1
Thread-3 (print_range): Current active threads: 3
Thread-3 (print_range): Current active threads: 2
...
...995 more lines of (Thread-3 (print_range): Current active threads: 2)
...
Thread-3 (print_range): Current active threads: 2
Finished
```

# b)
```
Thread-1 (print_range): 1
Thread-2 (print_range): -10
Thread-3 (print_range): Current active threads: 3
Thread-1 (print_range): 2
Thread-2 (print_range): -9
Thread-1 (print_range): 3
Thread-2 (print_range): -8
Thread-1 (print_range): 4
Thread-2 (print_range): -7
Thread-1 (print_range): 5
Thread-2 (print_range): -6
Thread-3 (print_range): Current active threads: 3
Thread-1 (print_range): 6
Thread-2 (print_range): -5
Thread-1 (print_range): 7
Thread-2 (print_range): -4
Thread-1 (print_range): 8
Thread-2 (print_range): -3
Thread-1 (print_range): 9
Thread-2 (print_range): -2
Thread-2 (print_range): -1
Thread-3 (print_range): All threads finished.
Finished
```

# c) 
```
Thread-2 (print_range): -10
Thread-1 (print_range): 1
Thread-3 (print_range): Current active threads: 3
Thread-2 (print_range): -9
Thread-2 (print_range): -8
Thread-1 (print_range): 2
Thread-1 (print_range): 3
Thread-1 (print_range): 4
Thread-1 (print_range): 5
Thread-2 (print_range): -7
Thread-2 (print_range): -6
Thread-1 (print_range): 6
Thread-2 (print_range): -5
Thread-2 (print_range): -4
Thread-2 (print_range): -3
Thread-2 (print_range): -2
Thread-2 (print_range): -1
Thread-3 (print_range): Current active threads: 2
Thread-1 (print_range): 7
Thread-1 (print_range): 8
Thread-1 (print_range): 9
Thread-3 (print_range): Current active threads: 1
Thread-3 (print_range): All threads finished.
Finished
```

# d)
```
Thread-2 (print_range): -10
Thread-1 (print_range): 1
Thread-3 (print_range): Current active threads: 4
Thread-2 (print_range): -9
Thread-2 (print_range): -8
Thread-1 (print_range): 2
Thread-1 (print_range): 3
Thread-1 (print_range): 4
Thread-1 (print_range): 5
Thread-2 (print_range): -7
Thread-2 (print_range): -6
Thread-1 (print_range): 6
Thread-3 (print_range): Current active threads: 4
Thread-2 (print_range): -5
Thread-2 (print_range): -4
Thread-2 (print_range): -3
Thread-2 (print_range): -2
Thread-2 (print_range): -1
Thread-1 (print_range): 7
Thread-1 (print_range): 8
Thread-1 (print_range): 9
Finished
```

# e)
```None of the above```
