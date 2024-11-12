def calculate_pyramid_height(number_of_blocks):
   
    height = 0
    total_boxes = 0
    
    while total_boxes + (height + 1) <= number_of_blocks:
        height += 1
        total_boxes += height
    
    return height
