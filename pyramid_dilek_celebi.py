def calculate_pyramid_height(number_of_blocks):
    used_before = 0
    height = 0
    while(number_of_blocks - used_before > height):
       height = height + 1
       used_before = (height*(height + 1)//2)
    return height
