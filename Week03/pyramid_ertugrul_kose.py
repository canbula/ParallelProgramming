def calculate_pyramid_height(blocks):
    h = 0
    while blocks > h:
        h += 1
        blocks -= h
    return h
