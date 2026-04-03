def calculate_pyramid_height(number_of_blocks):
    n = 0
    height = 0
    while True:
        block = (n * (n + 1)) // 2
        if block > number_of_blocks:
            break
        height = n
        n += 1
    return height
