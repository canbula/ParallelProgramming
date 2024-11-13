def calculate_pyramid_height(number_of_blocks):
    current_height = 0
    blocks_used = 0
    
    while blocks_used + current_height + 1 <= number_of_blocks:
        current_height += 1
        blocks_used += current_height
    
    return current_height
