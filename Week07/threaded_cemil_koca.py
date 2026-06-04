import threading
import random

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = [threading.Thread(target=func, args=args, kwargs=kwargs) for _ in range(n)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
        return wrapper
    return decorator

total_points = 0
inside_circle = 0
lock = threading.Lock()

NUM_POINTS_PER_THREAD = 100000
NUM_THREADS = 4

@threaded(NUM_THREADS)
def estimate_pi():
    global total_points, inside_circle
    local_total = 0
    local_inside = 0

    for _ in range(NUM_POINTS_PER_THREAD):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            local_inside += 1
        local_total += 1

    with lock:
        total_points += local_total
        inside_circle += local_inside

if __name__ == "__main__":
    estimate_pi()
    pi_estimate = 4 * inside_circle / total_points
    print(f"Total points: {total_points}")
    print(f"Points inside circle: {inside_circle}")
    print(f"Estimated Pi: {pi_estimate}")