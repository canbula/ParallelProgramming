import threading
import random
import time
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from queue import Queue


class Fork:
    def __init__(self, index: int, lock: threading.Lock, queue: Queue):
        self.index: int = index
        self.lock: threading.Lock = lock
        self.picked_up: bool = False
        self.owner: int = -1
        self.queue: Queue = queue

    def __enter__(self):
        return self

    def pickup(self, owner: int):
        if self.lock.acquire(timeout=1):
            self.owner = owner
            self.picked_up = True
            self.queue.put((self.index, "pickup"))
            return True
        else:
            return False

    def put_down(self):
        self.lock.release()
        self.picked_up = False
        self.owner = -1
        self.queue.put((self.index, "put down"))

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __str__(self):
        return f"F{self.index:2d} ({self.owner:2d})"


class Philosopher(threading.Thread):
    def __init__(self, index: int, left_fork: Fork, right_fork: Fork, spaghetti: int, queue: Queue):
        super().__init__()
        self.index: int = index
        self.left_fork: Fork = left_fork
        self.right_fork: Fork = right_fork
        self.spaghetti: int = spaghetti
        self.eating: bool = False
        self.finished: bool = False
        self.queue: Queue = queue

    def run(self):
        while self.spaghetti > 0:
            self.think()
            self.eat()
        print(f"P{self.index} left the table.")
        self.finished = True

    def think(self):
        time.sleep(1 + random.random() * 3)

    def eat(self):
        if self.finished:
            return

        while True:
            if self.left_fork.pickup(self.index):
                if self.right_fork.pickup(self.index):
                    break
                else:
                    self.left_fork.put_down()
            else:
                time.sleep(0.1)

        try:
            if self.finished:
                return

            self.spaghetti -= 1
            self.eating = True
            self.queue.put((self.index, "eating"))
            time.sleep(2 + random.random() * 2)
        finally:
            self.eating = False
            self.left_fork.put_down()
            self.right_fork.put_down()
            self.queue.put((self.index, "put down"))

    def __str__(self):
        return f"P{self.index:2d} ({self.spaghetti:2d})"


def animated_table(philosophers: list[Philosopher], forks: list[Fork], m: int):
    queue = Queue()

    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Dining Philosophers")
    philosopher_circles: list[plt.Circle] = [
        plt.Circle((0, 0), 0.2, color="black") for _ in range(len(philosophers))
    ]
    philosopher_texts: list[plt.Text] = [
        plt.Text(
            0,
            0,
            str(philosopher.index),
            horizontalalignment="center",
            verticalalignment="center",
        )
        for philosopher in philosophers
    ]
    fork_lines: list[plt.Line2D] = [
        plt.Line2D((0, 0), (0, 0), color="black") for _ in range(len(forks))
    ]
    fork_texts: list[plt.Text] = [
        plt.Text(
            0,
            0,
            str(fork.index),
            horizontalalignment="center",
            verticalalignment="center",
        )
        for fork in forks
    ]
    for philosopher_circle in philosopher_circles:
        ax.add_patch(philosopher_circle)
    for fork_line in fork_lines:
        ax.add_line(fork_line)
    for philosopher_text in philosopher_texts:
        ax.add_artist(philosopher_text)
    for fork_text in fork_texts:
        ax.add_artist(fork_text)

    def update(frame):
        while not queue.empty():
            index, action = queue.get()
            if action == "eating":
                philosopher_circles[index].set_color("red")
            elif action == "put down":
                philosopher_circles[index].set_color("black")
                for fork in forks:
                    if fork.owner == index:
                        fork_lines[fork.index].set_color("black")

        for i in range(len(philosophers)):
            philosopher_circles[i].center = (
                0.5 * math.cos(2 * math.pi * i / len(philosophers)),
                0.5 * math.sin(2 * math.pi * i / len(philosophers)),
            )
            philosopher_texts[i].set_position(
                (
                    0.9 * math.cos(2 * math.pi * i / len(philosophers)),
                    0.9 * math.sin(2 * math.pi * i / len(philosophers)),
                )
            )
            philosopher_texts[i].set_text(
                str(philosophers[i]) if philosophers[i].spaghetti > 0 else "X"
            )
            philosopher_circles[i].radius = 0.2 * philosophers[i].spaghetti / m
            fork_lines[i].set_data(
                (
                    0.5 * math.cos(2 * math.pi * i / len(philosophers)),
                    0.5 * math.cos(2 * math.pi * (i + 1) / len(philosophers)),
                ),
                (
                    0.5 * math.sin(2 * math.pi * i / len(philosophers)),
                    0.5 * math.sin(2 * math.pi * (i + 1) / len(philosophers)),
                ),
            )
            fork_texts[i].set_position(
                (
                    0.5 * math.cos(2 * math.pi * i / len(philosophers))
                    + 0.5 * math.cos(2 * math.pi * (i + 1) / len(philosophers)),
                    0.5 * math.sin(2 * math.pi * i / len(philosophers))
                    + 0.5 * math.sin(2 * math.pi * (i + 1) / len(philosophers)),
                )
            )
            fork_texts[i].set_text(str(forks[i]))
            if philosophers[i].eating:
                philosopher_circles[i].set_color("red")
            else:
                philosopher_circles[i].set_color("black")
            if forks[i].picked_up:
                fork_lines[i].set_color("red")
            else:
                fork_lines[i].set_color("black")
        return philosopher_circles + fork_lines + philosopher_texts + fork_texts

    ani = animation.FuncAnimation(
        fig, update, frames=range(100000), interval=10, blit=False
    )
    plt.show()


def table(philosophers: list[Philosopher], forks: list[Fork], m: int):
    while sum(philosopher.spaghetti for philosopher in philosophers) > 0:
        eating_philosophers: int = sum(
            philosopher.eating for philosopher in philosophers
        )
        print("\033[H\033[J")
        print("=" * (len(philosophers) * 16))
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


def main() -> None:
    n: int = 5
    m: int = 7
    forks: list[Fork] = [Fork(i, threading.Lock(), Queue()) for i in range(n)]
    philosophers: list[Philosopher] = [
        Philosopher(i, forks[i], forks[(i + 1) % n], m, forks[i].queue) for i in range(n)
    ]

    for i in range(n):
        right_fork_index = i
        left_fork_index = (i + n - 1) % n
        philosophers[i] = Philosopher(i, forks[right_fork_index], forks[left_fork_index], m, forks[i].queue)

    for philosopher in philosophers:
        philosopher.start()

    threading.Thread(target=table, args=(philosophers, forks, m), daemon=True).start()
    animated_table(philosophers, forks, m)

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
