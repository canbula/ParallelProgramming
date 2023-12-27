import threading
import time
import random
import tkinter as tk
import math

class Philosopher(threading.Thread):
    philosophers = []

    def __init__(self, index, left_fork, right_fork, max_philosophers_sem, gui_callback, fork_lines):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.max_philosophers_sem = max_philosophers_sem
        self.gui_callback = gui_callback
        self.figure = None
        self.background_circle = None
        self.state = "thinking"
        self.is_left_fork_taken = False
        self.is_right_fork_taken = False
        self.fork_lines = fork_lines
        self.eat_count = 0

    def update_gui(self):
        self.gui_callback(f"Philosopher {self.index} is {self.state}.")
        fill_color = "black"
        if self.state == "eating":
            fill_color = "red"
            self.eat_count += 1
            if self.eat_count >= 2:
                self.state = "full"

        background_oval = canvas.find_withtag(f"background_circle_{self.index}")[0]
        canvas.tag_raise(background_oval)
        canvas.tag_raise(self.figure)
        canvas.itemconfig(background_oval, fill=fill_color)
        status_text_id = canvas.find_withtag(f"status_text_{self.index}")
        canvas.itemconfig(status_text_id, text=self.state.capitalize())
        root.update()
        time.sleep(2)

    def run(self):
        while True:
            if self.state != "full":
                self.dine()

    def dine(self):
        think_time = random.uniform(1, 3)
        time.sleep(think_time)
        self.state = "thinking"
        self.update_gui()
        self.pick_up_forks()
        if self.state != "full":
            eat_time = random.uniform(1, 3)
            self.state = "eating"
            self.update_gui()
            time.sleep(eat_time)
            self.put_down_forks()
            time.sleep(1)

    def pick_up_forks(self):
        if self.state != "full":
            self.max_philosophers_sem.acquire()
            left_neighbor_index = (self.index + 1) % len(self.fork_lines)
            right_neighbor_index = (self.index - 1) % len(self.fork_lines)
            self.right_fork.acquire()
            self.state = "picking up right fork"
            self.is_right_fork_taken = True
            self.update_gui()
            line_right = canvas.create_line(self.fork_lines[self.index][0], self.fork_lines[self.index][1],
                                            self.fork_lines[right_neighbor_index][0],
                                            self.fork_lines[right_neighbor_index][1], width=2, fill="red",
                                            tags=f"line_{self.index}_right")
            canvas.tag_raise(line_right, self.figure)
            canvas.itemconfig(line_right, fill="red")
            self.left_fork.acquire()
            self.state = "picking up left fork"
            self.is_left_fork_taken = True
            self.update_gui()
            line_left = canvas.create_line(self.fork_lines[self.index][0], self.fork_lines[self.index][1],
                                           self.fork_lines[left_neighbor_index][0],
                                           self.fork_lines[left_neighbor_index][1], width=2, fill="red",
                                           tags=f"line_{self.index}_left")
            canvas.tag_raise(line_left, self.figure)
            canvas.itemconfig(line_left, fill="red")
            for philosopher in Philosopher.philosophers:
                canvas.tag_raise(philosopher.figure)
            left_neighbor_figure = canvas.find_withtag(f"philosopher_{left_neighbor_index}_icon")[0]
            right_neighbor_figure = canvas.find_withtag(f"philosopher_{right_neighbor_index}_icon")[0]
            canvas.tag_lower(line_left, left_neighbor_figure)
            canvas.tag_lower(line_right, right_neighbor_figure)
            background_circle_left = canvas.find_withtag(f"background_circle_{left_neighbor_index}")[0]
            background_circle_right = canvas.find_withtag(f"background_circle_{right_neighbor_index}")[0]
            canvas.tag_lower(line_left, background_circle_left)
            canvas.tag_lower(line_right, background_circle_right)
            canvas.tag_lower(line_left, background_circle_left)
            canvas.tag_lower(line_right, background_circle_right)

    def put_down_forks(self):
        self.right_fork.release()
        self.is_right_fork_taken = False
        line_id_right = canvas.find_withtag(f"line_{self.index}_right")
        canvas.delete(line_id_right)
        self.left_fork.release()
        self.is_left_fork_taken = False
        line_id_left = canvas.find_withtag(f"line_{self.index}_left")
        canvas.delete(line_id_left)
        self.max_philosophers_sem.release()
        if self.state == "full":
            self.state = "full"
            fill_color = "yellow"
        else:
            self.state = "putting down forks"
            fill_color = "black"
        self.update_gui()
        canvas.itemconfig(self.background_circle, fill=fill_color)
        canvas.itemconfig(self.figure)

def draw_figures(canvas):
    num_philosophers = 5
    angle = 360 / num_philosophers
    figures = []
    fork_lines = []
    for i in range(num_philosophers):
        x1 = 150 + 100 * math.cos(math.radians(i * angle))
        y1 = 150 + 100 * math.sin(math.radians(i * angle))
        x2 = 150 + 100 * math.cos(math.radians((i + 1) % num_philosophers * angle))
        y2 = 150 + 100 * math.sin(math.radians((i + 1) % num_philosophers * angle))
        canvas.create_line(x1, y1, x2, y2, width=2, fill="black", tags=f"fork_line_{i}")
    for i in range(num_philosophers):
        x_bg = 150 + 100 * math.cos(math.radians(i * angle))
        y_bg = 150 + 100 * math.sin(math.radians(i * angle))
        background_circle = canvas.create_oval(x_bg - 30, y_bg - 30, x_bg + 30, y_bg + 30, fill="black",
                                               tags=f"background_circle_{i}")
        x = 150 + 100 * math.cos(math.radians(i * angle))
        y = 150 + 100 * math.sin(math.radians(i * angle))
        figure = canvas.create_image(x, y, anchor=tk.CENTER, tags=f"philosopher_{i}_icon")
        figures.append(figure)
        fork_lines.append((x, y))
        canvas.create_text(x, y + 40, text="Thinking", fill="black", tags=f"status_text_{i}")
        canvas.create_text(x - 40, y, text=str(i), fill="black", font=("Arial", 10, "bold"))
    return figures, fork_lines

def gui_callback(message):
    text.insert(tk.END, message + "\n")
    text.see(tk.END)
    return "eating" in message

def start_simulation():
    num_philosophers = 5
    max_philosophers = 2
    forks = [threading.Lock() for _ in range(num_philosophers)]
    max_philosophers_sem = threading.Semaphore(max_philosophers)
    figures, fork_lines = draw_figures(canvas)
    philosophers = [
        Philosopher(i, forks[i], forks[(i + 1) % num_philosophers], max_philosophers_sem, gui_callback, fork_lines)
        for i in range(num_philosophers)
    ]
    for i, philosopher in enumerate(philosophers):
        philosopher.figure = figures[i]
        philosopher.background_circle = canvas.find_withtag(f"background_circle_{i}")[0]
        philosopher.start()


root = tk.Tk()
root.title("Dining Philosophers Problem")
start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.pack(pady=10)
canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()
text = tk.Text(root, height=20, width=50)
text.pack()
root.mainloop()
