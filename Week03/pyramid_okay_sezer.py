def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_needed = 1 # The number of blocks needed for the current level

    while number_of_blocks >= blocks_needed: 
        number_of_blocks -= blocks_needed # Use the needed blocks for the current level
        height += 1 # Move to the next level
        blocks_needed +=1 # The next level will require one more block than the current level
    return height