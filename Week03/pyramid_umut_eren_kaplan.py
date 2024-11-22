def calculate_pyramid_height(number_of_blocks):
    height = 0
    usedblocks = 0 

    while usedblocks < number_of_blocks:
        usedblocks +=1
        height+=1
        number_of_blocks -=height

    return height
