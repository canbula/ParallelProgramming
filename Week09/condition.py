import threading
import time

condition = threading.Condition()
shared_data = []


def producer():
    with condition:
        print("Producer: Adding item to shared_data.")
        time.sleep(1)
        shared_data.append("data")
        condition.notify()


def consumer():
    with condition:
        print("Consumer: Waiting for data...")
        condition.wait()
        print(f"Consumer: Got {shared_data.pop()}!")


consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()
