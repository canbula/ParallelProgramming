import random
import threading
from tqdm import tqdm


def throw_points(n):
    total_points = 0
    inner_points = 0
    progress_bar = tqdm(total=n)
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inner_points += 1
        total_points += 1
        progress_bar.update(1)

    pi = 4 * inner_points / total_points
    return pi, inner_points, total_points


if __name__ == "__main__":
    total_points = 10000000
    number_of_threads = 4
    number_of_points_per_thread = total_points // number_of_threads
    threads = []
    for i in range(number_of_threads):
        threads.append(
            threading.Thread(
                target=throw_points,
                args=(number_of_points_per_thread,),
                name=f"Throw Points - {i}",
            )
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
