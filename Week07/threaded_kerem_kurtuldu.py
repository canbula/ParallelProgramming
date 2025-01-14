import threading

def threaded(num_threads):
    class ThreadManager:
        def __init__(self, num_threads):
            self.num_threads = num_threads

        def __call__(self, func):
            def run_threads(*args, **kwargs):
                thread_list = []
                for n in range(self.num_threads):
                    t = threading.Thread(target=func, args=args, kwargs=kwargs, name=f"Thread-{n}")
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            return run_threads

    return ThreadManager(num_threads)
