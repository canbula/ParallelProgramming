import threading
import time

def threaded(number_of_threads):
    """
    A decorator to run a function in multiple threads.

    :param number_of_threads: The number of threads to create for the function.
    :type number_of_threads: int
    :return: A wrapped function that runs in the specified number of threads.
    :rtype: function
    """

    def decorator_of_thread(func):
        """
        Inner decorator to wrap the target function.

        :param func: The function to be executed in multiple threads.
        :type func: function
        :return: The wrapped function with threading enabled.
        :rtype: function
        """

        def _wrapper(*args, **kwargs):
            """
            Wrapper function to create, start, and synchronize threads.

            :param args: Positional arguments to pass to the target function.
            :param kwargs: Keyword arguments to pass to the target function.
            :return: None
            :rtype: None
            """
            threads = []
            for i in range(number_of_threads):
                threads.append(
                    threading.Thread(
                        target=func,
                        args=args,
                        kwargs=kwargs,
                        name=f"Thread - {i}",
                    )
                )
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        return _wrapper

    return decorator_of_thread


@threaded(16)
def func(task_name):
    print(f"{threading.current_thread().name} is starting task: {task_name}")
    time.sleep(2)
    print(f"{threading.current_thread().name} has finished task: {task_name}")


if __name__ == "__main__":
    func("Learning")
