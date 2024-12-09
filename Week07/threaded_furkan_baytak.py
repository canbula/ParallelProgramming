import threading

def threaded(n):
    """
    Decorator to create n threads for a function.

    Args:
        n (int): Number of threads to create.

    Returns:
        function: A decorated function that runs in n threads.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []

            # Function to be run in threads
            def target_func():
                func(*args, **kwargs)

            # Create and start threads
            for _ in range(n):
                thread = threading.Thread(target=target_func)
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

        return wrapper
    return decorator