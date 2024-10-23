def calculate_pyramid_height(number_of_blocks):
    height = 0
    count = 1
    while number_of_blocks >= 1:
        count += 1
        height += 1
        for i in range(0, count):
            number_of_blocks -= 1
            if number_of_blocks < 1:
                break
    return height
