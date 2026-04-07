def calculate_pyramid_height(number_of_blocks):
    height = 0
    needed_blocks = 1

    while number_of_blocks >= needed_blocks:
        number_of_blocks -= needed_blocks
        height += 1
        needed_blocks += 1

    return height
