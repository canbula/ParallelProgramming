def calculate_pyramid_height(number_of_blocks):
      height = 1
      while True:
        if((((height+1)*(height+2))/2) > number_of_blocks):
            return height                
        else:
            height=height+1
