import multiprocessing
import time
import os


"""
This file includes the following ways to create a process:
1. Create a process from a function
2. Create a process from a class
3. Create a process from a function and pass arguments
4. Create two processes and join them
5. Create a daemon process
6. Combine all the above and give names to the processes
"""


def process_0():
    print(
        f"This is process 0 with id {multiprocessing.current_process().pid} == {os.getpid()}"
    )


# 1. Create a process from a function
def create_process_from_function():
    def process_1():
        print(
            f"This is a process created from a function with id "
            f"{multiprocessing.current_process().pid} == {os.getpid()}"
        )
        time.sleep(5)

    p = multiprocessing.Process(target=process_1)
    p.start()


# 2. Create a process from a class
def create_process_from_class():
    class Process2(multiprocessing.Process):
        def __init__(self):
            super().__init__()

        def run(self):
            print(f"This is a process created from a class with id {os.getpid()}")
            time.sleep(5)

    p = Process2()
    p.start()


# 3. Create a process from a function and pass arguments
def create_process_from_function_and_pass_arguments():
    def process_3(s):
        print(
            f"This is a process created from a function "
            f"with id {os.getpid()} "
            f"and your argument is {s}"
        )
        time.sleep(5)

    #
    p = multiprocessing.Process(target=process_3, args=("Process 3",))
    p.start()


# 4. Create two processes and join them
def create_two_processes_and_join_them():
    def process_4_1():
        print(f"This is process 4_1 with id {os.getpid()}")
        time.sleep(1)
        print(f"Process 4_1 is done")

    def process_4_2():
        print(f"This is process 4_2 with id {os.getpid()}")
        time.sleep(3)
        print(f"Process 4_2 is done")

    def process_4_3():
        print(f"This is process 4_3 with id {os.getpid()}")
        print(f"I can only start after process 4_1 and process 4_2 are done")
        time.sleep(1)
        print(f"Process 4_3 is done")

    p1 = multiprocessing.Process(target=process_4_1)
    p2 = multiprocessing.Process(target=process_4_2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    p3 = multiprocessing.Process(target=process_4_3)
    p3.start()
    print(f"Process 4 is done")


# 5. Create a daemon process
def create_daemon_process():
    def process_5():
        print(f"This is a daemon process with id {os.getpid()}")
        time.sleep(5)

    p = multiprocessing.Process(target=process_5)
    p.daemon = True
    p.start()


if __name__ == "__main__":
    # get the start method of the multiprocessing module
    # print(multiprocessing.get_start_method())
    # change the start method of the multiprocessing module to fork
    multiprocessing.set_start_method("fork")
    # multiprocessing.set_start_method("spawn")
    # multiprocessing.set_start_method("forkserver")
    print(f"Main process id: {os.getpid()}")
    create_daemon_process()
    create_process_from_function()
    create_process_from_class()
    create_process_from_function_and_pass_arguments()
    create_two_processes_and_join_them()
