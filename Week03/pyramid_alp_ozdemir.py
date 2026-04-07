def calculate_pyramid_height(blocks):
    height = 0
    layer = 1
    while blocks >= layer:
        blocks = blocks - layer
        height += 1
        layer += 1

    return height
