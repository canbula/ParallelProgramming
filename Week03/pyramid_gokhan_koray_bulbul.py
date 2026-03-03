def calculate_pyramid_height(number_of_blocks):
    height = 1
    while True:
        if((a := a - height) <= height): return height
        height += 1
