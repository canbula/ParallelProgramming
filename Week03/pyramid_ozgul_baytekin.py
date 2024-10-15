def calculate_pyramid_height(number_of_blocks):
    height = 1  # there will be 1 block for the first level
    while number_of_blocks >= height:  
        number_of_blocks -= height  
        height += 1 
        
    return height -1


