def calculate_pyramid_height(blocks):
    height = 0

    for level in range(1, blocks + 1):
        if blocks >= level:
            blocks -= level
            height += 1
        else:
            break
    return height
