def calculate_pyramid_height(number_of_blocks):
    height = 0

    if number_of_blocks == 1:
        return number_of_blocks

    for i in range(1, number_of_blocks):
        if number_of_blocks >= i:
            number_of_blocks = number_of_blocks - i
            height += 1

    return height
