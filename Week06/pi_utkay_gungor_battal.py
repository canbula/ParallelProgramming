import random

def next_pi() :
    inner=0
    outer=0

    while True :
        x=random.random()
        y=random.random()

        if x**2 + y**2 <= 1 :
            inner +=1
        
        outer +=1

        pi = 4 * (inner / outer)
        yield pi
