import random
import time
from threading import Thread, Condition
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib


class JobsAndUsers:
    def __init__(self, number_of_users, number_of_resources, job_size):
        self.n = number_of_users
        self.r = number_of_resources
        self.m = job_size
        self.resources = [Condition() for _ in range(number_of_resources)]
        self.jobs = [job_size for _ in range(number_of_users)]
        self.queue = [0 for _ in range(number_of_resources)]
        matplotlib.use("TkAgg")
        plt.rcParams["figure.figsize"] = [8, 6]
        self.fig, self.axs = plt.subplots(1, 2, tight_layout=True)

    def user(self, i):
        print("Hi, I am user #%d" % i)
        while self.jobs[i] > 0:
            time.sleep(random.random())
            print("User #%d wants to start now" % i)
            r = self.queue.index(min(self.queue))
            self.queue[r] += 1
            print("User #%d is trying to get the resource #%d" % (i, r))
            if self.resources[r].acquire():
                print("User #%d has the resource #%d" % (i, r))
                time.sleep(random.random())
                self.jobs[i] -= 1
                self.queue[r] -= 1
                self.resources[r].notify()
                self.resources[r].release()
                print("User #%d has completed the job" % i)
            else:
                print("User #%d could not get the resource #%d" % (i, r))

    def axes_properties(self):
        self.axs[0].clear()
        self.axs[1].clear()
        self.axs[0].set_ylim([0, (self.n / self.r) + 1])
        self.axs[1].set_ylim([0, self.m])
        self.axs[0].set_title("Resources")
        self.axs[1].set_title("Jobs")

    def init(self):
        self.axes_properties()
        self.axs[0].bar([i for i in range(self.r)], self.queue)
        self.axs[1].bar([i for i in range(self.n)], self.jobs)

    def update(self, _):
        self.axes_properties()
        self.axs[0].bar([i for i in range(self.r)], self.queue)
        self.axs[1].bar([i for i in range(self.n)], self.jobs)
        if sum(self.jobs) == 0:
            quit()

    def draw(self):
        _ = FuncAnimation(self.fig, self.update, init_func=self.init, save_count=10)
        plt.show()


def main():
    n = 100
    r = 40
    m = 100
    jobs_and_users = JobsAndUsers(n, r, m)
    users = [Thread(target=jobs_and_users.user, args=(i,)) for i in range(n)]
    for user in users:
        user.start()
    jobs_and_users.draw()
    for user in users:
        user.join()


if __name__ == "__main__":
    main()
