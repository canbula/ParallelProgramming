def calculate_pyramid_height(blocks):
    layer = 0
    while blocks >= (layer + 1):
        layer += 1
        blocks -= layer

    return layer
