import threading
import time

def threaded(number_of_threads):
    """
    A decorator that runs a function concurrently using multiple threads.

    :param number_of_threads: The number of threads to spawn to run the decorated function.
    :type number_of_threads: int

    :return: A decorator to wrap a function with threaded execution.
    :rtype: function
    """
    def decorator(func):
        """
        The actual decorator that spawns the threads and runs the function.

        :param func: The function to be executed in multiple threads.
        :type func: function
        """
        def wrapper(task_name, *args, **kwargs):
            """
            Wrapper function that creates threads and runs the decorated function.

            :param task_name: The task name passed to the decorated function.
            :type task_name: str
            """
            threads = []
            for i in range(number_of_threads):
                thread = threading.Thread(target=func, args=(task_name,) + args, kwargs=kwargs, name=f"Thread-{i}")
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        return wrapper
    return decorator

@threaded(16)
def func(task_name):
    print(f"{threading.current_thread().name} is starting task: {task_name}")
    time.sleep(2)
    print(f"{threading.current_thread().name} has finished task: {task_name}")

if __name__ == "__main__":
    func("Learning")
