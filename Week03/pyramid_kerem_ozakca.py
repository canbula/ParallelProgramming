def calculate_pyramid_height(blocks):
    current_height = 0
  
    while blocks > current_height:
        current_height += 1
        blocks -= current_height
      
    return current_height
