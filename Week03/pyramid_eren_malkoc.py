# max block , height
# 1 , 1
# 3 , 2
# 6 , 3
# 10 , 4

def calculate_pyramid_height(number_of_blocks):
    height = 1

    while number_of_blocks >= height: 
        height += 1
        number_of_blocks -= height

    return height - 1
