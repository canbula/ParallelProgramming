def calculate_pyramid_height(number_of_blocs):
    a = 0
    p_block = 0
    while number_of_blocs > p_block:
        a +=1
        p_block += a
    if number_of_blocs == p_block:
        height = a 
    else:
        height = a-1
        
    return height