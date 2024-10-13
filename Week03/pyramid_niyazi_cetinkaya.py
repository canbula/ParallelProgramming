def calculate_pyramid_height(number_of_blocks: int) -> int:
    height = 0
    while True:
        if number_of_blocks > height*(height+1)/2:
            height = height + 1
        else:break
    return height

    
print(calculate_pyramid_height(7))
