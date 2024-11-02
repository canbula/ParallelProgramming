def calculate_pyramid_height(number_of_blocks):
    height = 0
    current_row_blocks = 1
    
    while number_of_blocks >= current_row_blocks:
        number_of_blocks -= current_row_blocks
        height += 1
        current_row_blocks += 1
    
    return height
