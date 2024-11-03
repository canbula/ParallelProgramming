def calculate_pyramid_height(blocks):
    height = 0
    total_blocks_used = 0
    
    while total_blocks_used + (height + 1) <= blocks:
        height += 1
        total_blocks_used += height
    
    return height
