import threading

def threaded(num_threads):
    class ThreadManager:
        def __init__(self, num_threads):
            self.num_threads = num_threads

        def __call__(self, func):
            def run_threads(*args, **kwargs):
                threads = []
                for i in range(self.num_threads):
                    thread = threading.Thread(target=func, args=args, kwargs=kwargs, name=f"Thread-{i}")
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

            return run_threads

    return ThreadManager(num_threads)
