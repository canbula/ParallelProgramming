import random

def next_pi():
   circle_points =0
   
   interval =50
    
   for square_points in range (interval):
      x = random.uniform(-1,1)
      y = random.uniform(-1,1)
      if(x**2 + y**2) < 1:
         circle_points +=1
      square_points +=1
    

      pi = 4*(circle_points/square_points)
      yield pi 
   

generator = next_pi()
iterator = iter(generator)
