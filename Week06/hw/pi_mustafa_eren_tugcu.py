import random 

def next_pi(): 
   
    i = 0
    n = 0 
    
    while True: 
        x = random.uniform(0,1)
        y = random.uniform(0,1)    
        r = x**2 + y**2 

        if r <= 1 : 
            i += 1 
        n += 1  
        
        
        yield 4 * i / n
        
