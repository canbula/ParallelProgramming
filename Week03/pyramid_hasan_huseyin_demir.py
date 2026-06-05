def calculate_pyramid_height(blocks):
    height = 0
    while(blocks >= 0):
        height += 1
        blocks -= height
    return height - 1
