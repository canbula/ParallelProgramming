def calculate_pyramid_height(number_of_blocks):
    n = 1
    height = 0
    
    while number_of_blocks >= n:
        height += 1
        number_of_blocks -= n
        n += 1

    return height
