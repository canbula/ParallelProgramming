import multiprocessing


class Sender(multiprocessing.Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    def run(self):
        self.pipe.send(f"{self.pid}: Message sent from {self.name}")
        self.pipe.close()


class Receiver(multiprocessing.Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    def run(self):
        print(f"{self.pid}: Message received: '{self.pipe.recv()}'")


class SenderReceiver(multiprocessing.Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    def run(self):
        self.pipe.send(f"{self.pid}: Message sent from {self.name}")
        print(f"{self.pid}({self.name}): Message received '{self.pipe.recv()}'")
        self.pipe.close()


def unidirectional_pipe():
    pipe_receive_end, pipe_send_end = multiprocessing.Pipe(False)
    sender = Sender(pipe_send_end)
    receiver = Receiver(pipe_receive_end)
    sender.start()
    receiver.start()
    sender.join()
    receiver.join()


def duplex_pipe():
    pipe = multiprocessing.Pipe(True)
    processes = [SenderReceiver(pipe[i % 2]) for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


if __name__ == '__main__':
    unidirectional_pipe()
    duplex_pipe()
