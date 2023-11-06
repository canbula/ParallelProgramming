import random 

def next_pi(): 
   
  
    i = 0
    n = 0 
    
    while True: 
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)    
        r = x**2 + y**2 

        if(r <= 1 ) : 
            i += 1 
        n += 1  
        
        pi = 4 * i / n 
        yield pi 
        
