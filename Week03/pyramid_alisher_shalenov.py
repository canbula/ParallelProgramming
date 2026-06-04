def calculate_pyramid_height(blocks):  # asd
    height = 0
    layer = 1

    while blocks >= layer:
        blocks -= layer
        height += 1
        layer += 1

    return height
