import hashlib
import os
import threading
import multiprocessing as mp

def text_to_md5(text: str) -> str:
    for i in range(2):
        text = hashlib.md5(text.encode()).hexdigest()
    return text


def decorator_for_you_to_implement(func):
    def wrapper(*args, **kwargs):
        passwd = kwargs["passwd"] if "passwd" in kwargs else args[0]
        start = kwargs["start"] if "start" in kwargs else args[1]
        end = kwargs["end"] if "end" in kwargs else args[2]

        cpu_count = os.cpu_count()

        step = int((end-start)/cpu_count)
        intervals = [_ for _ in range(start,end,step)]
        intervals.append(end)

        threads = []

        for i in range(cpu_count):
            start = intervals[i]
            end = intervals[i + 1]
            t = mp.Process(target=func, name=f"Thread {i}", args=(passwd, start, end))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    return wrapper

@decorator_for_you_to_implement
def guess_the_password(password: str, start: int, end: int) -> str:
    for i in range(start, end):
        if text_to_md5(str(i)) == password:
            return str(i)
    return ""


def main():
    passwd = "d0cc0430b803ff396f519753dabed75c"
    start = 10000000
    end = 100000000
    print(guess_the_password(passwd, start, end))


if __name__ == '__main__':
    main()
