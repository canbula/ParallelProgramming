# h * (h+1) / 2 = blocks
# h = -1 + sqrt(1 + 8 * blocks) / 2

import math

def calculate_pyramid_height(number_of_blocks):
    if number_of_blocks <= 0:
        return 0
    else: 
        height = int((-1 + math.sqrt(1 + 8 * number_of_blocks)) / 2)
    return height
