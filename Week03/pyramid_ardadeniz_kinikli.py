def calculate_pyramid_height(number_of_blocks):
    height = 0 
    blocks_used = 0
    counter = 1
    while blocks_used < number_of_blocks:
        blocks_used += counter 
        if blocks_used == number_of_blocks:
            height = counter
            break
        elif blocks_used > number_of_blocks:
            height = counter - 1
            break
        counter += 1     
    return height


