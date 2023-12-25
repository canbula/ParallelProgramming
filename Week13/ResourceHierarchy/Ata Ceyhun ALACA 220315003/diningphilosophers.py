import threading
import random
import time
import math
import pygame


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

    def __lt__(self, other):
        return self.index < other.index

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, spaghetti, num_philosophers, screen_width, screen_height):
        super().__init__()
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.spaghetti = spaghetti
        self.eating = False
        self.state = "T"
        angle = 2 * math.pi * index / num_philosophers
        circle_radius = min(screen_width, screen_height) // 3
        center_x, center_y = screen_width // 2, screen_height // 2
        self.x = int(center_x + circle_radius * math.cos(angle))
        self.y = int(center_y + circle_radius * math.sin(angle))

    def run(self):
        while self.spaghetti > 0:
            self.think()
            self.eat()

    def think(self):
        self.state = "Thinking"
        time.sleep(3 + random.random() * 3)

    def eat(self):
        with min(self.left_fork, self.right_fork)(self.index):
            time.sleep(5 + random.random() * 5)
            with max(self.left_fork, self.right_fork)(self.index):
                self.spaghetti -= 1
                self.eating = True
                self.state = "Eating"
                time.sleep(5 + random.random() * 5)
                self.eating = False
                self.state = "Thinking"

    def __str__(self):
        return f"P{self.index:2d} ({self.spaghetti:2d})"

def draw_philosophers(screen, philosophers):
    circle_radius = 30
    for philosopher in philosophers:
        color = (255, 0, 0) if philosopher.eating else (0, 0, 255)
        pygame.draw.circle(screen, color, (philosopher.x, philosopher.y), circle_radius)
        pygame.draw.circle(screen, (0, 0, 0), (philosopher.x, philosopher.y), circle_radius, 2)
        font = pygame.font.Font(None, 25)
        text = font.render(philosopher.state, True, (255, 255, 255))
        screen.blit(text, (philosopher.x - text.get_width() // 2, philosopher.y - text.get_height() // 2))

def animated_table_pygame(philosophers, forks, m):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dining Philosophers")
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 36)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        draw_philosophers(screen, philosophers)
        pygame.display.flip()
        clock.tick(60)
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Check if all philosophers have finished eating
        if all(philosopher.spaghetti == 0 for philosopher in philosophers):
            running = False
    # Display "Execution Finished" message
    screen.fill((255, 255, 255))
    text = font.render('Execution Finished', True, (0, 128, 0))
    text_rect = text.get_rect(center=(800 // 2, 600 // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(6000)
    pygame.quit()


def table(philosophers: list[Philosopher], forks: list[Fork], m: int):
    """
    Prints the table with the philosophers and forks.

    :param philosophers: The list of philosophers.
    :param forks: The list of forks.
    :param m: The amount of spaghetti each philosopher has.
    """
    while sum(philosopher.spaghetti for philosopher in philosophers) > 0:
        eating_philosophers: int = sum(
            philosopher.eating for philosopher in philosophers
        )
        # clear the screen
        print("\033[H\033[J")
        print("=" * (len(philosophers) * 16))
        # print a line for each philosopher if they are eating, thinking, or finished
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


def main():
    n = 5
    m = 7
    screen_width, screen_height = 800, 600
    forks = [Fork(i) for i in range(n)]
    philosophers = [
        Philosopher(i, forks[i], forks[(i + 1) % n], m, n, screen_width, screen_height) for i in range(n)
    ]
    for philosoper in philosophers:
        philosoper.start()
    threading.Thread(target=table, args=(philosophers, forks, m), daemon=True).start()
    animated_table_pygame(philosophers, forks, m)
    for philosoper in philosophers:
        philosoper.join()


if __name__ == "__main__":
    main()
