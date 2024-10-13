def calculate_pyramid_height(numOfBlocks):
    height = 0
    while ((height * (height + 1))/2) <= numOfBlocks:
        height+=1
    return height - 1
