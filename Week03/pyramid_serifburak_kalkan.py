def calculate_pyramid_height(number_of_blocks):

  for n in range(number_of_blocks): 
    if n*(n+1)/2 <= number_of_blocks: 
        height = n

  return height
