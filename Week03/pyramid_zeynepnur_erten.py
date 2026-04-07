def calculate_pyramid_height(number_of_blocks):
  i = 1
  height = 0
  while (number_of_blocks >= i) :
    number_of_blocks = number_of_blocks - i
    height += 1
    i += 1
    
  return height
