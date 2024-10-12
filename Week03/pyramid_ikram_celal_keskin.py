def calculate_pyramid_height(number_of_blocks:int):
    '''
    This function calculates the height of a pyramid that can be built with the given number of blocks.

    Args:
        number_of_blocks (int): The number of blocks that are available to build the pyramid.
    
    Returns:
        height (int): The height of the pyramid that can be built with the given number of blocks.
    '''
    
    if number_of_blocks < 0 or not isinstance(number_of_blocks, int):
        ValueError("The number of blocks must be a positive integer.")
    
    height = 0
    layer = 1

    while number_of_blocks >= layer:
        number_of_blocks -= layer
        layer += 1
        height += 1

    return height
