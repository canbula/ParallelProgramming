def calculate_pyramid_height(number_of_blocks):
    return int(((-1 + (1 + 8 * number_of_blocks) ** 0.5) / 2))
