import random

def next_pi() :
    num_in=0
    total_num=0

    while True :
        x=random.random()
        y=random.random()

        if x**2 + y**2 <= 1 :
            num_in +=1
        
        total_num +=1

        yield 4* num_in/total_num
