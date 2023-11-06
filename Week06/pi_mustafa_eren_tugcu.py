import random 

n = int(input("Enter the number of points: "))
i  = 0 

for _ in range(n): 
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)    
    
    r = x**2 + y**2 

    if(r <= 1 ) : 
        print("inside the circle")
        i += 1 
    else : 
        print("outside the circle") 

pi = 4 * i / n 
print("pi = ", pi  , "i=" , i , "n=" , n)    
