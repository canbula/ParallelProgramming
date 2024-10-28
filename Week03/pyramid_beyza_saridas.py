def calculate_pyramid_height(number_of_blocks):
    total_blocks = 0
    height = 0
    
    while total_blocks < number_of_blocks:
        height += 1
        total_blocks += height
        
        if total_blocks == number_of_blocks:
            return height
