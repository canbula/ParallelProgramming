import threading
import random
import time
from queue import Queue

class Fork:
    def __init__(self, index: int):
        self.index: int = index
        self.lock: threading.Lock = threading.Lock()
        self.picked_up: bool = False
        self.owner: int = -1

    def __enter__(self):
        return self

    def __call__(self, owner: int):
        if self.lock.acquire():
            self.owner = owner
            self.picked_up = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        self.picked_up = False
        self.owner = -1

    def __str__(self):
        return f"F{self.index:2d} ({self.owner:2d})"

class DiningPhilosophers:
    def __init__(self, forks):
        self.fork_queue = Queue()
        for fork in forks:
            self.fork_queue.put(fork)

    def pick_up_forks(self):
        left_fork = self.fork_queue.get()
        right_fork = self.fork_queue.get()
        return left_fork, right_fork

    def put_down_forks(self, left_fork, right_fork):
        self.fork_queue.put(left_fork)
        self.fork_queue.put(right_fork)

class Philosopher(threading.Thread):
    def __init__(self, index: int, dining_philosophers: DiningPhilosophers, m: int):
        super().__init__()
        self.index: int = index
        self.dining_philosophers: DiningPhilosophers = dining_philosophers
        self.spaghetti: int = m
        self.state: str = "Thinking"  # Initial state is Thinking
        self.times_eaten: int = 0

    def run(self):
        while self.times_eaten < 7:
            self.think()
            self.eat()

    def think(self):
        time.sleep(3 + random.random() * 3)
        self.state = "Hungry"  # After thinking, philosopher becomes hungry again

    def eat(self):
        left_fork, right_fork = self.dining_philosophers.pick_up_forks()

        with left_fork(self.index), right_fork(self.index):
            time.sleep(5 + random.random() * 5)
            self.spaghetti -= 1
            self.state = "Eating"
            time.sleep(5 + random.random() * 5)
            self.state = "Thinking"


        self.dining_philosophers.put_down_forks(left_fork, right_fork)
        self.times_eaten += 1

    def __str__(self):
        return f"P{self.index:2d} ({self.state}, Spaghetti: {self.spaghetti:2d})"


def print_table(philosophers):
    header = "Philosopher | Spaghetti | Eating | Hungry"
    divider = "-" * len(header)
    rows = [f"{philosopher}" for philosopher in philosophers]

    print(header)
    print(divider)
    for row in rows:
        print(row)
    print(divider)
    print()


def main() -> None:
    n: int = 5
    m: int = 7
    forks: list[Fork] = [Fork(i) for i in range(n)]
    dining_philosophers = DiningPhilosophers(forks)
    philosophers: list[Philosopher] = [
        Philosopher(i, dining_philosophers, m) for i in range(n)
    ]

    for philosopher in philosophers:
        philosopher.start()

    while any(philosopher.is_alive() for philosopher in philosophers):
        print_table(philosophers)
        time.sleep(1)

    print_table(philosophers)


if __name__ == "__main__":
    main()