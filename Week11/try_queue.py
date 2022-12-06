import multiprocessing
import random
import string
import time


class NewProcess(multiprocessing.Process):
    def __init__(self, q, name=None):
        super().__init__()
        self.q = q
        self.name = name if name else "Bora Canbula"

    def run(self):
        self.q.put(f"Hello from {self.name}")


class PasswordGenerator(multiprocessing.Process):
    def __init__(self, q, v, length=8, chars=string.ascii_letters + string.digits + string.punctuation):
        super().__init__()
        self.daemon = True
        self.q = q
        self.v = v
        self.length = length
        self.chars = chars

    def run(self):
        while True:
            with self.v.get_lock():
                self.v.value += 1
            self.q.put("".join(random.choice(self.chars) for _ in range(self.length)))
            if self.v.value > 100:
                break


def password_generator():
    q = multiprocessing.Queue()
    v = multiprocessing.Value('i', 0)
    p = PasswordGenerator(q, v)
    p.start()
    i = 0
    time.sleep(1)
    while not q.empty():
        i += 1
        print(q.get(), v.value, i)
        time.sleep(0.1)


def main():
    names = [
        "Isaac Newton",
        "Albert Einstein",
        "Marie Curie",
        "Charles Darwin",
        "Nikola Tesla",
        "Galileo Galilei",
        "Stephen Hawking",
        "Leonardo da Vinci",
        "Michael Faraday",
        "Thomas Edison",
        "Alexander Graham Bell",
        "Benjamin Franklin",
        "James Watt",
        "Louis Pasteur",
        "Ada Lovelace",
        "Alan Turing",
        "Blaise Pascal",
        "Rene Descartes",
        "Johannes Kepler"
    ]
    random.shuffle(names)
    q = multiprocessing.Queue()
    processes = [NewProcess(q, names[i]) for i in range(multiprocessing.cpu_count())]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    main()
    password_generator()
