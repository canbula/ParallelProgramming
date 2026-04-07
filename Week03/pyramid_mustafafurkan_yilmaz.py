def calculate_pyramid_height(number_of_blocks):
    height = 0
    layer = 1
    while number_of_blocks >= layer:
        number_of_blocks -= layer
        height += 1
        layer += 1
    return height
