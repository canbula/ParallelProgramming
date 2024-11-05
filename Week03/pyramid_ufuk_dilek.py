def calculate_pyramid_height(number_of_blocks):
    iteration = 0
    total = 0
    while True:
        if number_of_blocks < total:
            break
        else:
            iteration += 1
            total += iteration
    return iteration - 1
