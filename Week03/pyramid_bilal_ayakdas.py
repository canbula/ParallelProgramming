def calculate_pyramid_height(number_of_blocks: int) -> int:
    """
    Calculate the height of a pyramid given the number of blocks.
    :param number_of_blocks: The total number of blocks available to build the pyramid.
    :type number_of_blocks: int
    :raises ValueError: If the number of blocks is less than or equal to 0.
    :return: The maximum height of the pyramid that can be built.
    :rtype: int
    """
    if number_of_blocks <= 0:
        raise ValueError("Number of blocks must be greater than 0")
    
    height, layer = 0, 1
    
    while number_of_blocks >= layer:
        number_of_blocks -= layer
        height += 1
        layer += 1
        
    return height

