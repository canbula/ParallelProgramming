import enum
import multiprocessing
import random
import time

PHILOSOPHER_COUNT = 5


class State(enum.Enum):
    THINKING = 0
    HUNGRY = 1
    EATING = 2


global_sems = [multiprocessing.Semaphore(0) for _ in range(PHILOSOPHER_COUNT)]
global_states = [
    multiprocessing.Value("i", State.THINKING.value)
    for _ in range(PHILOSOPHER_COUNT)
]
global_transition_lock = multiprocessing.Lock()
global_io_lock = multiprocessing.Lock()


def next_n(n: int) -> int:
    return (n + 1) % PHILOSOPHER_COUNT


def prev_n(n: int) -> int:
    return (n - 1) % PHILOSOPHER_COUNT


class Philosopher:
    def __init__(
            self,
            n: int,
            *,
            semaphores: list[multiprocessing.Semaphore],
            states: list[multiprocessing.Value],
            state_lock: multiprocessing.Lock,
            io_lock: multiprocessing.Lock,
            spaghetti: int = 5
    ):
        self.n = n
        self.spaghetti = spaghetti

        self.sems = semaphores
        self.states = states
        self.state_lock = state_lock
        self.io_lock = io_lock

    def __repr__(self):
        return f"Philosopher({self.n}, spaghetti={self.spaghetti})"

    def __str__(self):
        return f"Philosopher {self.n}"

    def next_n(self):
        return next_n(self.n)

    def prev_n(self):
        return prev_n(self.n)

    def _try_to_release_semaphore(self, *, n: int = None):
        if n is None:
            n = self.n

        if (
                self.states[n].value == State.HUNGRY.value
                and self.states[next_n(n)].value != State.EATING.value
                and self.states[prev_n(n)].value != State.EATING.value
        ):
            self.sems[n].release()
            self.states[n].value = State.EATING.value

    def _pick_forks_up_blocking(self):
        if self.states[self.n].value != State.THINKING.value:
            return

        self.states[self.n].value = State.HUNGRY.value

        with self.state_lock:
            self._try_to_release_semaphore()
        self.sems[self.n].acquire()
        with self.io_lock:
            print(f"{self} picked up both forks.")

    def _put_forks_down(self):
        with self.state_lock:
            self.states[self.n].value = State.THINKING.value
            self._try_to_release_semaphore(n=self.next_n())
            self._try_to_release_semaphore(n=self.prev_n())
            self.spaghetti -= 1
            with self.io_lock:
                print(
                    f"{self} put down both forks. "
                    f"{self.spaghetti} sessions left."
                )

    def _eat(self):
        assert self.states[self.n].value == State.EATING.value

        t = 5 + random.random() * 5
        with self.io_lock:
            print(f"{self} will eat for {t:.2f}s.")
        time.sleep(t)

    def _think(self):
        assert self.states[self.n].value == State.THINKING.value

        t = 3 + random.random() * 3
        with self.io_lock:
            print(f"{self} will think for {t:.2f}s.")
        time.sleep(t)

    def run(self):
        while self.spaghetti > 0:
            self._think()
            self._pick_forks_up_blocking()
            self._eat()
            self._put_forks_down()
        with self.io_lock:
            print(f"{self} is done eating!")


def main():
    philosophers = [
        Philosopher(
            i,
            semaphores=global_sems,
            states=global_states,
            state_lock=global_transition_lock,
            io_lock=global_io_lock,
        )
        for i in range(PHILOSOPHER_COUNT)
    ]
    processes = [multiprocessing.Process(target=p.run) for p in philosophers]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
