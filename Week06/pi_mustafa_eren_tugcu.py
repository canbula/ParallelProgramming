import random 


def next_pi(): 
    n = int(input("Enter the number of points: "))
    i  = 0 

    for _ in range(n): 
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)    
    
        r = x**2 + y**2 

        if(r <= 1 ) : 
            i += 1 
        
        pi = 4 * i / n 
