
def calculate_pyramid_height(number_of_blocks):
    """
    Calculates the maximum height of a pyramid that can be built with a given number of blocks.
    
    The pyramid is built layer by layer, where each layer requires an increasing number of blocks.
    The first layer requires 1 block, the second layer 2 blocks, and so on. The function subtracts 
    the blocks needed for each layer until there are not enough blocks for the next layer.
    
    Parameters:
    number_of_blocks (int): The total number of blocks available to build the pyramid.

    Returns:
    int: The maximum height of the pyramid that can be built.
    If the input is invalid (not an integer), an error message is printed.
    """
  
    # Initial height and number of blocks required for the first layer
    height = 0
    number = 1
    
    # Check if the input is an integer
    if isinstance(number_of_blocks, int):
        # If the number of blocks is less than 3, a pyramid cannot be built
        if number_of_blocks < 3:
            return 0
        else:
            # Continue building the pyramid as long as there are enough blocks for the next layer
            while number_of_blocks >= number:
                number_of_blocks -= number
                number += 1
                height += 1
            return height
    else:
        print("Invalid parameter! Parameter must be an integer")
        return None
      
