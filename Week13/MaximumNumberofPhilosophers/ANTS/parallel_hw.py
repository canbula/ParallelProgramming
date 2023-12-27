import threading
import random
import time
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
            print(f"{self} is picked up by Philosopher {owner}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        self.picked_up = False
        self.owner = -1
        print(f"{self} is released.")

    def __str__(self):
        return f"F{self.index:2d} ({'P' + str(self.owner) if self.picked_up else ' '})"


class Philosopher(threading.Thread):
    def __init__(self, index: int, left_fork: Fork, right_fork: Fork, spaghetti: int, semaphore: threading.Semaphore):
        super().__init__()
        self.index: int = index
        self.left_fork: Fork = left_fork
        self.right_fork: Fork = right_fork
        self.spaghetti: int = spaghetti
        self.eating: bool = False
        self.semaphore: threading.Semaphore = semaphore

    def run(self):
        while self.spaghetti > 0:
            self.think()
            self.eat()

    def think(self):
        print(f"{self} is thinking.")
        time.sleep(3 + random.random() * 3)
        print(f"{self} has finished thinking.")

    def eat(self):
        with self.semaphore:
            with self.left_fork(self.index):
                time.sleep(5 + random.random() * 5) 
                with self.right_fork(self.index):
                    self.spaghetti -= 1
                    self.eating = True
                    print(f"{self} is eating.")              
                    time.sleep(5 + random.random() * 5)
                    print(f"{self} has finished eating.")
                    self.eating = False

    def __str__(self):
        return f"P{self.index:2d} ({self.spaghetti:2d})"


def animated_table(philosophers: list[Philosopher], m: int):
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Dining Philosophers")

    philosopher_circles: list[plt.Circle] = [
        plt.Circle((0.5 * math.cos(2 * math.pi * i / len(philosophers)), 0.5 * math.sin(2 * math.pi * i / len(philosophers))), 0.2, color="black") for i in range(len(philosophers))
    ]

    philosopher_names: list[plt.Text] = [
        plt.text(
            0.5 * math.cos(2 * math.pi * i / len(philosophers)),
            0.5 * math.sin(2 * math.pi * i / len(philosophers)),
            f"{philosophers[i].index}",
            ha="center",
            va="center",
            color="white"
        ) for i in range(len(philosophers))
    ]

    for philosopher_circle in philosopher_circles:
        ax.add_patch(philosopher_circle)

   


    def update(frame):
        nonlocal philosophers
        for i in range(len(philosophers)):
            philosopher_circles[i].center = (
                0.5 * math.cos(2 * math.pi * i / len(philosophers)),
                0.5 * math.sin(2 * math.pi * i / len(philosophers)),
            )

            if philosophers[i].eating:
                philosopher_circles[i].set_edgecolor("red")
                philosopher_circles[i].set_facecolor("red")
            else:
                philosopher_circles[i].set_edgecolor("black")
                philosopher_circles[i].set_facecolor("black")

            philosopher_circles[i].radius = 0.2 * philosophers[i].spaghetti / m

            philosopher_names[i].set_position((0.5 * math.cos(2 * math.pi * i / len(philosophers)), 0.5 * math.sin(2 * math.pi * i / len(philosophers))))

            if sum(philosopher.spaghetti for philosopher in philosophers) == 0:
                ani.event_source.stop()
                exit(0)

        return philosopher_circles + philosopher_names

    ani = animation.FuncAnimation(
        fig, update, frames=range(100000), interval=10, blit=False
    )
    plt.show()

    
    philosopher_circles: list[plt.Circle] = [
        plt.Circle((0.5 * math.cos(2 * math.pi * i / len(philosophers)), 0.5 * math.sin(2 * math.pi * i / len(philosophers))), 0.2, color="black") for i in range(len(philosophers))
    ]
    
    for philosopher_circle in philosopher_circles:
        ax.add_patch(philosopher_circle)


def main() -> None:
    n: int = 5
    m: int = 5
    forks: list[Fork] = [Fork(i) for i in range(n)]
    
    maximum_number_of_philosopher = threading.Semaphore(2)
    
    philosophers: list[Philosopher] = [
        Philosopher(i, forks[i], forks[(i + 1) % n], m, maximum_number_of_philosopher) for i in range(n)
    ]
    
    for philosopher in philosophers:
        philosopher.start()
        
    threading.Thread( args=(philosophers, m), daemon=True).start()
    animated_table(philosophers, m)
    
    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()