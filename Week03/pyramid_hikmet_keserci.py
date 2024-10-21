def calculate_pyramid_height(number_of_blocks):
    height = 0
    block_used = 0
    layer = 1

    while block_used + layer <= number_of_blocks:
        block_used += layer
        height += 1
        layer += 1

    missing_blocks = layer - (number_of_blocks - block_used) if block_used != number_of_blocks else 0

    return height, missing_blocks
