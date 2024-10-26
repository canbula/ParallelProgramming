def calculate_pyramid_height(number_of_blocks):
    height = 0
    for i in range(0,number_of_blocks):
        number_of_blocks=number_of_blocks - (height+1) 
        height += 1
        i += 1
        if height >= number_of_blocks :
            break
    return height
