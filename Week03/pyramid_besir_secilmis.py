def calculate_pyramid_height(number_of_blocks):
    height = 0
    n = 0
    while True:
        blocks_needed = (n * (n + 1)) // 2
        if blocks_needed > number_of_blocks:
            break
        height = n
        n += 1
    return height
