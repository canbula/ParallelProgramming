import threading
import time

semaphore = threading.Semaphore(2)


def task(thread_id):
    print(f"T-{thread_id}: Waiting for semaphore")
    semaphore.acquire()
    print(f"T-{thread_id}: Acquired semaphore!")
    time.sleep(1)
    semaphore.release()
    print(f"T-{thread_id}: Released semaphore!")


threads = [threading.Thread(target=task, args=(i,)) for i in range(6)]

for t in threads:
    t.start()

for t in threads:
    t.join()
