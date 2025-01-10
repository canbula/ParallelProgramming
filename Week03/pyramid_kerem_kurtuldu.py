def calculate_pyramid_height(blocks):
    # Initialize height and the number of blocks needed for the first level
    height = 0
    current_level = 1

    # Continue building levels as long as there are enough blocks
    while blocks >= current_level:
        blocks -= current_level  # Use blocks for the current level
        height += 1              # Increment the pyramid's height
        current_level += 1       # Move to the next level

    return height  # Return the total height of the pyramid
