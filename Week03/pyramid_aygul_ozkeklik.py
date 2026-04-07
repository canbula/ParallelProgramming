def calculate_pyramid_height(number_of_blocks):
    height = 0
    total_blocks = 0

    while total_blocks + height < number_of_blocks:
        height += 1
        total_blocks = (height * (height + 1))//2
    
    return height

print(calculate_pyramid_height(10))
print(calculate_pyramid_height(28))
print(calculate_pyramid_height(55))
