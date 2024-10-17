def calculate_pyramid_height(number_of_blocks):
    height = 0 
    total_blocks = 0  # Total number of blocks used so far
    while total_blocks + (height + 1) <= number_of_blocks: 
        height += 1  
        total_blocks += height  # Add the number of blocks in the new level to the total
    return height 
