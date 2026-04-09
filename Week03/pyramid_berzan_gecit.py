def calculate_pyramid_height(number_of_blocks):
    height = 0
    row = 1
    while number_of_blocks >= row:
        number_of_blocks -= row
        height += 1
        row += 1
    return height
