def calculate_pyramid_height(number_of_blocks):
    height = 0
    total = 0
    i = 1

    while total + i <= number_of_blocks:
        total += i
        height += 1
        i += 1

    return height
