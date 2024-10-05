def calculate_pyramid_height(number_of_blocks):
  height = 0
  while number_of_blocks > 0:
    height += 1
    number_of_blocks -= height
  return height
