def calculate_pyramid_height(number_of_blocks):
    if not isinstance(number_of_blocks, int) or number_of_blocks <= 0:
        return "Please enter a positive integer value."
    
    total_blocks = 0
    height = 0
    
    while total_blocks < number_of_blocks:
        height += 1
        total_blocks += height
        
        if total_blocks == number_of_blocks:
            return height
    
    # If total_blocks exceeds number_of_blocks, the pyramid cannot be formed.
    return "A pyramid cannot be formed with this number of blocks."
