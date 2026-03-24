def calculate_pyramid_height(number_of_blocks):
    height = 0
    used_blocks = 0

    while True:
        next_layer = height + 1
        if used_blocks + next_layer > number_of_blocks:
            break
        used_blocks += next_layer
        height += 1

    return height
