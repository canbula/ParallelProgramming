def calculate_pyramid_height(blocks):
    
    height = 0
    blocks_needed = 1
    
    while blocks >= blocks_needed:
        blocks -= blocks_needed
        height += 1
        blocks_needed += 1
    return height
