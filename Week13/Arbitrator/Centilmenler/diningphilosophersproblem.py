import threading
import random
import time

# Fork class
class Fork:
    def __init__(self, index: int):
        self.index: int = index
        self.lock: threading.Lock = threading.Lock()
        self.picked_up: bool = False
        self.owner: int = -1

    # This function acquires the lock for the fork
    def __enter__(self):
        return self

    # Function picks up the fork and assign its owner
    def __call__(self, owner: int):
        if self.lock.acquire():
            self.owner = owner
            self.picked_up = True
        return self

    # This functions releases the forks
    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        self.picked_up = False
        self.owner = -1

    def __str__(self):
        return f"F{self.index:2d} ({self.owner:2d})"

# Arbitrator class
class Arbitrator:
    def __init__(self, max_allowed: int):
        self.max_allowed = max_allowed
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.allowed = 0

    # It represents permission
    def acquire(self):
        with self.lock:
            while self.allowed >= self.max_allowed:
                self.condition.wait()
            self.allowed += 1

    # It represents permissions.
    def release(self):
        with self.lock:
            self.allowed -= 1
            self.condition.notify()

# Philosopher class
class Philosopher(threading.Thread):
    def __init__(self, index: int, left_fork: Fork, right_fork: Fork, spaghetti: int, arbitrator: Arbitrator):
        super().__init__()
        self.index: int = index
        self.left_fork: Fork = left_fork
        self.right_fork: Fork = right_fork
        self.spaghetti: int = spaghetti
        self.eating: bool = False
        self.arbitrator: Arbitrator = arbitrator

    # If there is spaghetti on the plate, it shows that the philosopher can think and eat.
    def run(self):
        while self.spaghetti > 0:
            self.think()
            self.eat()

    # It represents thinking time
    def think(self):
        time.sleep(3 + random.random() * 3)

    # It represents eating time
    def eat(self):
        self.arbitrator.acquire()
        with self.left_fork(self.index):
            time.sleep(random.random() * 5)
            with self.right_fork(self.index):
                self.spaghetti -= 1
                self.eating = True
                time.sleep(random.random() * 5)
                self.eating = False
        self.arbitrator.release()

    def __str__(self):
        return f"P{self.index:2d} ({self.spaghetti:2d})"

# This function prints the status of philosophers
def table(philosophers: list[Philosopher], forks: list[Fork], m: int):
    while sum(philosopher.spaghetti for philosopher in philosophers) > 0:
        eating_philosophers: int = sum(
            philosopher.eating for philosopher in philosophers
        )
        # Clear the screen
        print("\033[H\033[J")
        print("=" * (len(philosophers) * 16))
        # print a line for each philosopher if they are eating, thinking, or done
        print(
            "         ",
            "             ".join(
                ["E" if philosopher.eating else "T" for philosopher in philosophers]
            ),
        )
        print("       ".join(map(str, forks)), "     ", forks[0])
        print(
            "      ",
            "       ".join(map(str, philosophers)),
            "      : ",
            str(eating_philosophers),
        )
        time.sleep(0.1)

# Main function
def main() -> None:
    n: int = 5
    m: int = 7
    arbitrator = Arbitrator(2)  # It allows 2 philosophers to eat simultaneously.

    forks: list[Fork] = [Fork(i) for i in range(n)]
    philosophers: list[Philosopher] = [
        Philosopher(i, forks[i], forks[(i + 1) % n], m, arbitrator) for i in range(n)
    ]
    for philosopher in philosophers:
        philosopher.start()
    threading.Thread(target=table, args=(philosophers, forks, m), daemon=True).start()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()
