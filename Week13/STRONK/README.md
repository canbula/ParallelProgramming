# Multithreading Queue in Python and Dining Philosophers Problem
## Multithreading Queue
> In Python, the queue module is designed to facilitate secure communication between multiple threads by offering a thread-safe FIFO data structure. This structure ensures a synchronized flow of data, preventing potential issues like race conditions and data corruption.

>Usage of queue.Queue():
When working with Python, the queue module becomes a valuable tool for managing communication between threads. It introduces a thread-safe First-In-First-Out (FIFO) data structure, safeguarding against race conditions and data corruption by enabling synchronized data flow.

```python
import queue
import threading

# Create a queue instance
q = queue.Queue()

# Add items to the queue
q.put(1)
q.put(2)
q.put(3)

# Retrieve items from the queue
print(q.get())  # Output: 1
print(q.get())  # Output: 2
print(q.get())  # Output: 3
```
![image](https://github.com/Musa-Sina-Ertugrul/Solution_Dining_P/assets/102359522/df48d7cd-f71e-4037-9ee2-6460edd6ebcd)

## Dining Philosophers Problem
> The Dining Philosophers problem stands as a classical synchronization challenge within the realm of computer science, shedding light on the complexities associated with resource allocation and concurrent processes. Originating from the mind of E.W. Dijkstra in 1965, this problem aims to showcase the difficulties in preventing deadlock and ensuring the secure distribution of limited resources among various processes.

>Imagine a scenario where a group of philosophers is arranged around a circular dining table, each pair of adjacent philosophers having a bowl of spaghetti between them. These philosophers alternate between two activities: contemplating and eating.

>In this scenario, each philosopher engages in two fundamental actions:

>Contemplating: Philosophers spend their time lost in thought until hunger strikes.

>Eating:  To satisfy their hunger, a philosopher requires two forks—one for the left hand and one for the right. They pick up the necessary forks, dine for a while, and then return the forks to the table.

>The inherent challenge emerges from the following conditions:

>Every philosopher requires two forks to eat.
Philosophers only take one fork at a time.
Direct communication between philosophers is absent; they communicate solely through shared forks
The objective is to devise a solution, be it an algorithm or a set of rules, that permits the philosophers to dine without succumbing to deadlock. Deadlock occurs when each philosopher holds one fork and waits indefinitely for the other, resulting in a situation where all philosophers are immobilized and unable to proceed.

> The Dining Philosophers problem serves as a paradigm in concurrent programming, providing a tangible example of the hurdles associated with resource sharing, synchronization, and deadlock avoidance in systems featuring multiple competing processes. Solutions to this problem often showcase various synchronization techniques and strategies for efficiently and safely managing shared resources among concurrent processes.

![image](https://github.com/Musa-Sina-Ertugrul/Solution_Dining_P/assets/102359522/b8800459-e358-4e74-b81f-75153db01f57)

## Pesudo Solution using Multithreading Queue
>
> The provided code illustrates how the Dining Philosophers problem is addressed through the utilization of threads (implemented as the Philosopher class) and a queue for fork access control. Philosophers, represented by instances of the Philosopher class, seamlessly alternate between thinking and eating, ensuring the acquisition of both left and right forks before commencing their meal. The queue serves as a synchronization mechanism among philosophers, mitigating conflicts during fork access.
>This methodology effectively manages shared resources, specifically the forks, among philosophers, thereby averting deadlocks and guaranteeing equitable resource access. Through this example, it is demonstrated how Python's multithreading queue (queue.Queue()) can be applied to resolve synchronization challenges such as the Dining Philosophers problem in a manner that ensures thread safety.
>
>Here's an example pesudo implementation using Python's threading and queue modules:

```python
import threading
import time
import queue

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork, queue):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.queue = queue

    def run(self):
        while True:
            self.think()
            self.queue.put((self.name, 'hungry'))
            self.eat()

    def think(self):
        print(f"{self.name} is thinking.")
        time.sleep(1)

    def eat(self):
        self.queue.put((self.name, 'waiting'))
        self.queue.put((self.name, 'waiting for fork', self.left_fork))
        self.queue.put((self.name, 'waiting for fork', self.right_fork))

        while True:
            if self.queue.get() == (self.name, 'forks available'):
                break

        print(f"{self.name} is eating.")
        time.sleep(1)

        self.queue.put((self.name, 'done eating', self.left_fork))
        self.queue.put((self.name, 'done eating', self.right_fork))

        print(f"{self.name} finished eating.")
        time.sleep(1)
        self.queue.put((self.name, 'thinking'))

def main():
    num_philosophers = 5
    forks = [queue.Queue() for _ in range(num_philosophers)]
    philosophers = []

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher = Philosopher(f"Philosopher {i + 1}", left_fork, right_fork, forks[i])
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()

if __name__ == "__main__":
    main()
```
> Code Explanation: 

* 1.Controller Class
The Controller class manages access to the forks using two queues (q_right and q_left) and a lock (l) for synchronization.
The __enter__ method is called when entering a with block, acquiring the lock.
The __exit__ method is called when exiting the with block, releasing the lock.
The __call__ method adds a philosopher to both the left and right queues.

* 2.Fork Class:
The Fork class represents a fork with an index, a lock for synchronization, and status information (picked up, owner).
The __enter__ and __exit__ methods allow the fork to be used in a with statement.
The __call__ method is used to pick up the fork and set the owner.
The __str__ method returns a string representation of the fork.

* 3.Philiosopher Class: 
The Philosopher class extends threading.Thread and represents a philosopher thread.
The run method is the main loop where philosophers think and eat.
The think method simulates thinking by sleeping for a random time.
The eat method checks for available forks, picks them up, and simulates eating.
The __check_left and __check_right methods check the availability of left and right forks using queues.
The __str__ method returns a string representation of the philosopher.

* 4.Animated Table Function:
This function creates an animated visualization of the dining philosophers problem using Matplotlib.
It uses circles and lines to represent philosophers and forks, updating their positions and states in each frame.
The update function is called in each frame to update the visualization.

* 5.Table Function:
This function prints the current state of philosophers and forks in a tabular format.
It uses the terminal to display the state dynamically.

* 6.Main Function:
The main function sets up the dining philosophers scenario with a specified number of philosophers (n) and spaghetti portions (m).
It creates forks, a controller, and a list of philosophers with corresponding forks.
The table function is run in a separate thread to print the current state of philosophers and forks.
The animated_table function is called to create an animated visualization of the dining process.





![image](https://github.com/Musa-Sina-Ertugrul/Solution_Dining_P/assets/102359522/e8a78821-bd21-4bc5-838f-706114d9ccec)

