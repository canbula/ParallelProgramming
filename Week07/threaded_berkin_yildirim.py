import threading

def repeat_in_threads(times):
    """
    Decorator to execute a function multiple times in separate threads.
    """
    def apply_decorator(target_function):
        def execute_in_threads(*args, **kwargs):
            thread_list = []
            for _ in range(times):
                t = threading.Thread(target=target_function, args=args, kwargs=kwargs)
                thread_list.append(t)
                t.start()
            for t in thread_list:
                t.join()
        execute_in_threads.__name__ = target_function.__name__
        execute_in_threads.__doc__ = target_function.__doc__
        execute_in_threads.__module__ = target_function.__module__
        return execute_in_threads
    return apply_decorator
