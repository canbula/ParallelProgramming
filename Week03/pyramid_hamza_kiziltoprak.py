def calculate_pyramid_height(number_of_blocks):
    height = 0    
    i = 1
    while number_of_blocks > 0:
        number_of_blocks -= i
        i += 1
        height += 1
        if number_of_blocks - i < 0:
            break
    return height
