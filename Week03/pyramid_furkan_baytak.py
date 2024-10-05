import math

def calculate_pyramid_height(number_of_blocks):
    # 1 + 2 + 3 +...+ height = number_of_blocks
    # height (height + 1) / 2 = number_of_blocks
    # height**2 + height − 2 * number_of_blocks = 0
    # return int((-1 + math.sqrt(1 + 8 * number_of_blocks)) / 2)

    height = 0
    count = 0

    while count + (height + 1) <= number_of_blocks:
        height += 1
        count += height

    return height
