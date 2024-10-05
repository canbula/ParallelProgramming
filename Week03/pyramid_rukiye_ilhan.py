def calculate_pyramid_height(number_of_blocks):
    used_block = 0
    height = 0
    while(number_of_blocks - used_block > height):
       height = height + 1
       used_block = (height*(height + 1)//2)
    return height
