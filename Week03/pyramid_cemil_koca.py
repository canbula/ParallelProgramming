def calculate_pyramid_height(number_of_blocks):
    height = 0
    remaining = number_of_blocks

    while remaining >= height + 1:
        height += 1
        remaining -= height

    return height