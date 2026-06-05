def calculate_pyramid_height(number_of_blocks):
    height = 0
    needed = 1
    while number_of_blocks >= needed:
        number_of_blocks -= needed
        height += 1
        needed += 1
    return height
