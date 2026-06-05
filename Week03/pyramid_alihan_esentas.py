def calculate_pyramid_height(blockNumber):
  height  = 0

  while blockNumber > height:
    height += 1 
    blockNumber -= height
  return height
