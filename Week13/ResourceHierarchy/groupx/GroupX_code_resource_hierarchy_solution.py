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
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        self.picked_up = False
        self.owner = -1

    def __str__(self):
        return f"F{self.index:2d} ({self.owner:2d})"

class Philosopher(threading.Thread):
    def __init__(self, index: int, left_fork: Fork, right_fork: Fork, spaghetti: int):
        super().__init__()
        self.index: int = index
        self.left_fork: Fork = left_fork
        self.right_fork: Fork = right_fork
        self.spaghetti: int = spaghetti

    def run(self):
        while self.spaghetti > 0:
            self.think()
            self.eat()

    def think(self):
        update_visual(self.index, 'thinking', self.spaghetti)
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        first_fork, second_fork = sorted([self.left_fork, self.right_fork], key=lambda fork: fork.index)
        with first_fork(self.index), second_fork(self.index):
            update_visual(self.index, 'eating', self.spaghetti)
            print(f"Philosopher {self.index} starts eating.")
            time.sleep(random.uniform(1, 2))
            print(f"Philosopher {self.index} finishes eating.")
            self.spaghetti -= 1
            update_visual(self.index, 'thinking', self.spaghetti)

# Görselleştirme için yeni fonksiyonlar
states = ['thinking'] * 5
spaghetti_remaining = [3] * 5  # Başlangıçta her filozof için 3 spaghetti
positions = [(0.5 * math.cos(2 * math.pi * i / 5), 0.5 * math.sin(2 * math.pi * i / 5)) for i in range(5)]
fig, ax = plt.subplots()

def update_visual(philosopher, status, spaghetti):
    global states, spaghetti_remaining
    states[philosopher] = status
    spaghetti_remaining[philosopher] = spaghetti

def draw_circle(ax, pos, radius, color):
    circle = plt.Circle(pos, radius, color=color)
    ax.add_artist(circle)

def animate(i):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    for i, (state, spaghetti) in enumerate(zip(states, spaghetti_remaining)):
        color = 'yellow' if state == 'eating' else 'gray'
        radius = 0.1 * spaghetti  # Yemek miktarına göre dairenin büyüklüğü
        draw_circle(ax, positions[i], radius, color)
        ax.text(positions[i][0], positions[i][1], str(i), ha='center', va='center')

def main():
    forks = [Fork(i) for i in range(5)]
    philosophers = [Philosopher(i, forks[i], forks[(i + 1) % 5], 3) for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()