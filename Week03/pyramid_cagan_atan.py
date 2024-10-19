def calculate_pyramid_height(number_of_blocks : int) -> int:
    if number_of_blocks < 0:
        raise ValueError("The number of blocks must be a non-negative integer.")
    height = 0
    while number_of_blocks > 0:
        height += 1
        number_of_blocks -= height
    # If the number of blocks is negative (the layer is missing blocks), the height is decremented by 1.
    if number_of_blocks < 0:
        height -= 1
    return height
