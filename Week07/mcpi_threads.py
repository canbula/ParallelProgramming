import random
import threading


def throw_darts(num_darts, index):
    global results
    num_hits = 0
    for i in range(num_darts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            num_hits += 1
    results[index] = num_hits
    print(f"Thread {index} finished and got {num_hits} hits: {num_hits/num_darts*4}")


def main():
    num_darts = 100000000
    num_threads = 16
    num_darts_per_thread = num_darts // num_threads
    threads = []
    global results
    for i in range(num_threads):
        results.append(0)
        t = threading.Thread(target=throw_darts, args=(num_darts_per_thread, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    num_hits = sum(results)
    print(f"Main thread finished and got {num_hits} hits: {num_hits/num_darts*4}")


if __name__ == '__main__':
    results = []
    main()
