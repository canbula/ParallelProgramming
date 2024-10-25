def calculate_pyramid_height(number_of_blocks):
    height = 0  # Start with height 0
    
    # Loop until blocks required for the next level exceed available blocks
    while (height * (height + 1)) // 2 <= number_of_blocks:
        height += 1
    
    return height - 1  # Subtract 1 to get the maximum achievable height


