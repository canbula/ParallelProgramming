def calculate_pyramid_height(number_of_blocks):
    """
    Calculate the height of a pyramid that can be built with a given number of blocks.

    The function determines how many complete layers (height) can be formed
    using the provided number of blocks. Each layer requires a number of blocks
    equal to the layer number (1 block for the first layer, 2 blocks for the
    second layer, etc.).

    :param number_of_blocks: The total number of blocks available to build the pyramid.
    :type number_of_blocks: int
    :return: The maximum height of the pyramid that can be built.
    :rtype: int

    :raises ValueError: If `number_of_blocks` is less than 0.

    Example:

    calculate_pyramid_height(6)
    3
    calculate_pyramid_height(20)
    5
    """
    if number_of_blocks < 0:
        raise ValueError("Number of blocks must be non-negative.")

    height_of_pyramid = 0
    block_counter = 0

    while number_of_blocks >= (block_counter + (height_of_pyramid + 1)):
        block_counter += height_of_pyramid + 1
        height_of_pyramid += 1

    return height_of_pyramid
