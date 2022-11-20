import hashlib
import threading
import os


def text_to_md5(text: str) -> str:
    for i in range(2):
        text = hashlib.md5(text.encode()).hexdigest()
    return text


def decorator_for_you_to_implement(func):
    def wrapper(*args, **kwargs):
        for _ in range(os.cpu_count()):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.start()
        return func(*args, **kwargs)
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
