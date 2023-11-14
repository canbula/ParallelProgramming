import random 


def next_pi():
    inner = 0
    total = 0
    while True:
        total += 1
        x = random.random()
        y = random.random()
        inner_test = (x**2) + (y**2) <= 1

        if inner_test == True:
            inner += 1
        

        my_pi = (inner/total) * 4 


        yield my_pi
