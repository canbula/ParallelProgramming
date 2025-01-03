def calculate_pyramid_height(blocks):
    height = 0
    required_blocks = 1
    
    while blocks >= required_blocks:
        blocks -= required_blocks
        height += 1
        required_blocks += 1
    
    return height
