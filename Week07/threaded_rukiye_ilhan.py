import threading
def threaded(func):
    def wrapper(*args, **kwargs):
        # İlk argüman string float olarqlk laındasa bu aşamda doğrudan int oalrak kullanılacak şekilde ayarlanır
        n = int(args[0])
        threads = []
        for _ in range(n):
            t = threading.Thread(target=func, args=args[1:], kwargs=kwargs)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    return wrapper
