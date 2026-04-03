def calculate_pyramid_height(number_of_blocks):
    # Input precautions
    if (not isinstance(number_of_blocks, int)) or (number_of_blocks < 0):
        raise TypeError("number_of_blocks must be a non-negative whole integer.")
    
    height = 1
    while True:
        if(number_of_blocks := number_of_blocks - height) <= height: return height
        height += 1
