def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_needed = 1
    
    while number_of_blocks >= blocks_needed:
        number_of_blocks -= blocks_needed
        height += 1
        blocks_needed += 1
        
    return height
