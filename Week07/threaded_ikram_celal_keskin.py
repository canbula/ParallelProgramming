import threading

def threaded(n:int) ->callable:
    """
    A decorator that runs a function using multiple threads.

    :param n: Number of threads to create
    :type n: int
    :return: A decorator function for threading
    :rtype: function
    """
    # if n < 1 or not isinstance(n, int):
    #     raise ValueError("Not Valid call of the decorator")
    
    def decorator(func:callable) ->callable:
        """
        An inner decorator function that wraps the original function with threads.

        :param func: The original function to be run in threads
        :type func: function
        :return: A wrapper function that runs with threads
        :rtype: function
        """
        if not hasattr(func, "__call__"):
            raise ValueError("Not Valid Function")

        def wrapper(*args, **kwargs)->None:
            """
            A wrapper function that runs the function with multiple threads.

            :param args: Positional arguments to pass to the function
            :param kwargs: Keyword arguments to pass to the function
            """
 
            all_threads = []
            try:                
                for _ in range(n):

                        one_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                        all_threads.append(one_thread)
                        one_thread.start()
                
                for thread in all_threads:
                    thread.join()

            except threading.ThreadError as te:
                print(te)
        
        return wrapper

    return decorator
