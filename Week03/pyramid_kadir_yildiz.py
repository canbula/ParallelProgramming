def calculate_pyramid_height(blocks_number):
    height = 0

    for blocks_needed in range(1, blocks_number + 1):
        if blocks_number < blocks_needed:
            break
        blocks_number -= blocks_needed
        height += 1

    return height
