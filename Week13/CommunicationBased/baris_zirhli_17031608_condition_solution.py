import threading
import time
import random


class Philosopher(threading.Thread):
    def __init__(self, philosopher_id: int, eat_max):
        super().__init__()
        self.philosopher_id = philosopher_id
        self.eat_max = eat_max
        self.eat_count: int = 0

    def run(self):
        while self.eat_count < self.eat_max:
            self.think()
            self.pick_forks()
            self.eat()
            self.put_forks()

    def think(self):
        time.sleep(random.uniform(1, 3))
        print(f"Philosopher {self.philosopher_id} is thinking.")

    def pick_forks(self):
        with forks[self.philosopher_id]:
            while True:
                if fork_owners[self.philosopher_id] == -1:
                    fork_owners[self.philosopher_id] = self.philosopher_id
                    break
                else:
                    forks[self.philosopher_id].wait()

        with forks[(self.philosopher_id + 1) % num_philosophers]:
            while True:
                right_neighbor = (
                    self.philosopher_id + 1
                ) % num_philosophers  # round table
                if fork_owners[right_neighbor] == -1:
                    fork_owners[right_neighbor] = self.philosopher_id
                    break
                else:
                    forks[right_neighbor].wait()

    def eat(self):
        time.sleep(random.uniform(1.5, 3.0))
        print(f"Philosopher {self.philosopher_id} is eating.")
        self.eat_count += 1

    def put_forks(self):
        with forks[self.philosopher_id]:
            fork_owners[self.philosopher_id] = -1
            forks[self.philosopher_id].notify_all()

        with forks[(self.philosopher_id + 1) % num_philosophers]:
            right_neighbor = (self.philosopher_id + 1) % num_philosophers
            fork_owners[right_neighbor] = -1
            forks[right_neighbor].notify_all()


if __name__ == "__main__":
    eat_max: int = 3
    num_philosophers = 5
    forks = [threading.Condition() for _ in range(num_philosophers)]
    fork_owners = [-1] * num_philosophers
    philosophers = [Philosopher(i, eat_max) for i in range(num_philosophers)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

    for philosopher in philosophers:
        print(f" philosopher:{philosopher.philosopher_id} ate {philosopher.eat_count}")
