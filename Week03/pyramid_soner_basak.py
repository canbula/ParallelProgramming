def calculate_pyramid_height(number_of_blocks):
  height = 0
  required_blocks = 1
  
  while number_of_blocks >= required_blocks:
    number_of_blocks -= required_blocks
    height += 1
    required_blocks += 1
    
  return height
