import threading
import time


'''
This file includes the following ways to create a thread:
1. Create a thread from a function
2. Create a thread from a class
3. Create a thread from a function and pass arguments
4. Create two threads and join them
5. Create a daemon thread
6. Combine all the above and give names to the threads
'''


# 1. Create a thread from a function
def create_thread_from_function():
    def thread_1():
        print(f"This is a thread created from a function "
              f"with id {threading.get_native_id()}")

    t = threading.Thread(target=thread_1)
    t.start()


# 2. Create a thread from a class
def create_thread_from_class():
    class Thread2(threading.Thread):
        def __init__(self):
            super().__init__()

        def run(self):
            print(f"This is a thread created from a class "
                  f"with id {threading.get_native_id()}")

    t = Thread2()
    t.start()


# 3. Create a thread from a function and pass arguments
def create_thread_from_function_and_pass_arguments():
    def thread_3(s):
        print(f"This is a thread created from a function "
              f"with id {threading.get_native_id()} "
              f"and your argument is {s}")

    t = threading.Thread(target=thread_3, args=("Thread 3",))
    t.start()


# 4. Create two threads and join them
def create_two_threads_and_join_them():
    def thread_4_1():
        print(f"This is thread 4_1 with id {threading.get_native_id()}")
        time.sleep(1)
        print(f"Thread 4_1 is done")

    def thread_4_2():
        print(f"This is thread 4_2 with id {threading.get_native_id()}")
        time.sleep(3)
        print(f"Thread 4_2 is done")

    def thread_4_3():
        print(f"This is thread 4_3 with id {threading.get_native_id()}")
        print(f"I can only start after thread 4_1 and thread 4_2 are done")
        time.sleep(1)
        print(f"Thread 4_3 is done")

    t1 = threading.Thread(target=thread_4_1)
    t2 = threading.Thread(target=thread_4_2)
    t3 = threading.Thread(target=thread_4_3)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.start()


# 5. Create a daemon thread
def create_daemon_thread():
    def thread_5():
        print(f"This is a daemon thread with id {threading.get_native_id()}")
        while True:
            time.sleep(1)
            print(f"I am still alive because I am a daemon thread")
        print(f"I will never be printed because I am a daemon thread")

    def thread_6():
        print(f"This is a non-daemon thread with id {threading.get_native_id()}")
        time.sleep(5)
        print(f"I am done therefore the program will exit")

    t1 = threading.Thread(target=thread_5)  # or t1 = threading.Thread(target=thread_5, daemon=True)
    t2 = threading.Thread(target=thread_6)
    t1.daemon = True
    t1.start()
    t2.start()


# 6. Combine all the above and give names to the threads
def combine_all_and_give_names_to_threads():
    def a_thread_to_join_1():
        print(f"This is thread 1 with id {threading.get_native_id()}")
        time.sleep(1)
        print(f"Thread 1 is done")

    def a_thread_to_join_2():
        print(f"This is thread 2 with id {threading.get_native_id()}")
        time.sleep(3)
        print(f"Thread 2 is done")

    def a_thread_after_join():
        print(f"This is thread 3 with id {threading.get_native_id()}")
        print(f"I can only start after thread 1 and thread 2 are done")
        time.sleep(1)
        print(f"Thread 3 is done")

    def a_daemon_thread_running_in_background():
        print(f"This is a daemon thread with id {threading.get_native_id()}")
        while True:
            time.sleep(1)
            print(f"I am still alive because I am a daemon thread")

    def a_non_daemon_thread():
        print(f"This is a non-daemon thread with id {threading.get_native_id()}")
        time.sleep(5)
        print(f"The program will exit when no non-daemon threads are left")

    t1 = threading.Thread(target=a_thread_to_join_1, name="Thread 1")
    t2 = threading.Thread(target=a_thread_to_join_2, name="Thread 2")
    t3 = threading.Thread(target=a_thread_after_join, name="Thread 3")
    t4 = threading.Thread(target=a_daemon_thread_running_in_background, name="Daemon Thread", daemon=True)
    t5 = threading.Thread(target=a_non_daemon_thread, name="Non-Daemon Thread")
    t4.start()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.start()
    t5.start()


if __name__ == "__main__":
    print(f"This is the main thread with id: {threading.get_native_id()}")
    create_thread_from_function()
    create_thread_from_class()
    create_thread_from_function_and_pass_arguments()
    create_two_threads_and_join_them()
    create_daemon_thread()
    combine_all_and_give_names_to_threads()
