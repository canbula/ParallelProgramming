import threading

def threaded(n):
    """
    A decorator that accepts an integer argument 'n' and creates, 
    starts, and synchronizes 'n' threads from the decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            
            # 1. Create and start 'n' number of threads
            for _ in range(n):
                thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                thread.start()
                threads.append(thread)
                
            # 2. Synchronize the threads by waiting for them to finish
            for thread in threads:
                thread.join()
                
        return wrapper
    return decorator

# --- Example usage for testing ---
if __name__ == "__main__":
    import time
    
    # Decorate a sample function to run in 3 threads
    @threaded(3)
    def sample_task(task_name):
        print(f"[{threading.current_thread().name}] Starting {task_name}...")
        time.sleep(1)
        print(f"[{threading.current_thread().name}] Finished {task_name}.")

    print("Main program started.")
    sample_task("Data Processing")
    print("Main program finished. All threads successfully synchronized.")
