def calculate_pyramid_height(number_of_blocks):
    height = 0
    for i in range(number_of_blocks):
        height += 1
        if height * (height + 1) / 2 > number_of_blocks:
            height -= 1
            break
    return height
