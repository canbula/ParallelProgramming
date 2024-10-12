def calculate_pyramid_height(number_of_blocks):
    height = 0
    total_blocks = 0
    while total_blocks <= number_of_blocks:
        height+=1
        total_blocks += height
    return height - 1
