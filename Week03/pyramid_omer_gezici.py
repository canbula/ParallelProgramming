def calculate_pyramid_height(number_of_blocks):
    a1 = 0
    a2 = 1
    sum1 = 0
    sum2 = 0
    num = 0
    while(True):
        a1+=1
        sum1 += a1
        a2+=1
        sum2 += a2
        num+=1
        if(number_of_blocks>=sum1 and number_of_blocks<=sum2):
                height=num
                return height

print(calculate_pyramid_height(1))
print(calculate_pyramid_height(2))
print(calculate_pyramid_height(6))
print(calculate_pyramid_height(20))
print(calculate_pyramid_height(100))
print(calculate_pyramid_height(1000))
print(calculate_pyramid_height(10000))
print(calculate_pyramid_height(100000))
