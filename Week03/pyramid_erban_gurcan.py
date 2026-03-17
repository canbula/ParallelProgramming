def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_needed_for_next_layer = 1
    
 while number_of_blocks >= blocks_needed_for_next_layer:
        
        number_of_blocks -= blocks_needed_for_next_layer
        height += 1
        blocks_needed_for_next_layer += 1
        
 return height
