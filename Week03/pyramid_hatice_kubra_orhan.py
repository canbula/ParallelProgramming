
def calculate_pyramid_height(number_of_blocks):
    if number_of_blocks < 0:
        raise ValueError("Block count must be non-negative.")

    height = 0      
    count = 0       

    while count + (height + 1) <= number_of_blocks:
        height += 1                
        count += height   

    return height


#test

print(calculate_pyramid_height(6))  # 3
print(calculate_pyramid_height(20))  # 5
