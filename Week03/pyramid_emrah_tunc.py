def calculate_pyramid_height(number_of_blocks: int) -> int:
    height = 0
    blocks_needed = 1
    
    while number_of_blocks >= blocks_needed:
        height += 1
        number_of_blocks -= blocks_needed
        blocks_needed += 1
        
    return height
