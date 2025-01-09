def calculate_pyramid_height(number_of_blocks):
    height = 0
    count = 0
    while count <= number_of_blocks:
        height += 1
        count += height
    return height - 1
