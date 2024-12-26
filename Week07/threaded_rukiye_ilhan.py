import threading
def threaded(func):
    def wrapper(*args, **kwargs):
        threads = []
        for _ in range(args[0]):  # args paramtre listesindeki 0. eleman n değeridir dolaylı olarak elde edildi
            t = threading.Thread(target=func, args=args[1:], kwargs=kwargs)#args=args[1:] 1.indeksetiki 'Merhaba Dinbya' yazısını basar
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    return wrapper
