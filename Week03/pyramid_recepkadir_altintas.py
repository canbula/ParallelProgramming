def calculate_pyramid_height(number_of_blocks : int) -> int :
    height = 0
    block_for_floor = 1
    while number_of_blocks >= block_for_floor :
        number_of_blocks -= block_for_floor
        height += 1
        block_for_floor += 1

    return height  
