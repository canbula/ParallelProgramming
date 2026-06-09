import threading
import random
import time

class Fork:
    def __init__(self, index: int):
        self.index = index
        self.lock = threading.Lock()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()

class Philosopher(threading.Thread):
    def __init__(self, index: int, left_fork: Fork, right_fork: Fork, spaghetti: int):
        super().__init__()
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.spaghetti = spaghetti

    def run(self):
        while self.spaghetti > 0:
    
            time.sleep(random.uniform(0.01, 0.05))

            if self.index % 2 != 0:
                first_fork = self.left_fork
                second_fork = self.right_fork
            else:
                first_fork = self.right_fork
                second_fork = self.left_fork

            first_fork.acquire()
            second_fork.acquire()

            if self.spaghetti > 0:
                self.spaghetti -= 1
                time.sleep(random.uniform(0.01, 0.05))

            second_fork.release()
            first_fork.release()
