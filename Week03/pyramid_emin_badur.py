def calculate_pyramid_height(number_of_blocks):
    height = 1    

    if number_of_blocks <= 0 :
        raise ValueError("Number of blocks must be positive ")
    
    while number_of_blocks > height + 1 :
        height += 1 
        number_of_blocks -= height

    return height
